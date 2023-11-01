# from logging import raiseExceptions
# Standard Library
import datetime
import os
import posixpath
import uuid
import webbrowser

# Third Party Stuff
import pytz
import requests
import yadisk  # type: ignore
from yadisk import YaDisk  # type: ignore

# My Stuff
from log_worker import LogWorker
from settings import Settings
from warninger import ok

# import log_worker


class YDWorker:
    def __init__(self, log: LogWorker):
        self.settings_obj = Settings()
        self.settings = self.settings_obj.data["yandex"]
        token = self.GetToken()
        self.y = YaDisk(token=token)
        if not (self.y.check_token()):
            token = self.NewToken()
            self.y = YaDisk(token=token)
        self.l = log
        self.yandex_root = self.settings["destination_folder"]
        self.days_l = self.settings["delete_dest_older_than"]

    def file_upload(self, source_file_path: str):
        to_dir = self.yandex_root + "/Zipped"

        try:
            self.y.mkdir(self.yandex_root)
        except yadisk.exceptions.PathExistsError:
            pass

        try:
            self.y.mkdir(to_dir)
        except yadisk.exceptions.PathExistsError:
            pass

        dest_file_path = posixpath.join(to_dir, os.path.basename(source_file_path))

        # self.l.log(f'Uploading {source_file_path} to {dest_file_path}')
        try:
            self.y.upload(
                source_file_path,
                dest_file_path,
                overwrite=False,
                timeout=self.settings["upload_timeout"],
            )
        except yadisk.exceptions.PathExistsError:
            self.l.log(
                f"File {source_file_path} in directory {dest_file_path} already exists"
            )
        # except yadisk.exceptions.PathExistsError: self.l.log(f'Insufficient Storage')
        except Exception as e:
            self.l.log(f"Error: {e.args[0]}")

    def recursive_upload(self, from_dir):
        if not self.y.exists(self.yandex_root):
            self.y.mkdir(self.yandex_root)

        dirname = os.path.basename(from_dir)
        dest_folder = posixpath.join(self.yandex_root, dirname)
        # to_dir = self.yandex_root + f"/{dirname}"

        walk = os.walk(from_dir)
        self.l.debug(f"Walking {from_dir=}")
        for root, dirs, files in walk:
            self.l.debug(f"Walk found {root=} {dirs=} {files=}")
            p = root.split(from_dir)[1].strip(os.path.sep)
            # dest_folder = posixpath.join(to_dir, p)

            try:
                self.y.mkdir(dest_folder)
            except yadisk.exceptions.PathExistsError:
                pass

            files.sort()
            for file in files:
                path = os.path.join(root, file)

                dest_file_path = posixpath.join(dest_folder, file)
                self.l.debug(
                    f"!!! creating dest_file_path from {dest_folder=} and {file=} = {dest_file_path=} \n{p=} {root=} {path=}"
                )
                p_sys = p.replace("/", os.path.sep)
                source_file_path = os.path.join(from_dir, p_sys, file)

                # check file is not locked
                if not os.access(source_file_path, os.R_OK):
                    continue

                # check free space
                size = os.stat(path).st_size / 1024 / 1024 / 1024
                freespace = self.free_space()
                root_size = self.folder_size(self.yandex_root)

                if (
                    size >= freespace
                    and root_size > 0
                    and self.settings["delete_oldest_on_no_space"]
                ):
                    s = format(size, ".2f")
                    text = f"Not enough space for file: {path} size: {s} \
                    Gb, free space: {freespace} Gb, deleting oldest files"
                    self.l.error(text)
                    self.clean_by_size(size)
                if size >= freespace and root_size == 0:
                    text = f"There is no enough space on the Yandex Disk to upload file {path}. \
                    And folder {self.yandex_root} is empty. Uploading of this file is canceled"
                    self.l.error(text)
                    continue

                text = f"Uploading {source_file_path} to {dest_file_path}"
                self.l.log(text)
                try:
                    self.y.upload(
                        source_file_path,
                        dest_file_path,
                        overwrite=False,
                        timeout=self.settings["upload_timeout"],
                    )
                    text = f"Upload complete, removing {source_file_path}"
                    self.l.log(text)
                    # remove file after upload
                    if self.settings["delete_source_after_upload"]:
                        os.remove(source_file_path)
                        text = f"File {source_file_path} removed"
                        self.l.log(text)
                    ok()
                except yadisk.exceptions.PathExistsError:
                    text = f"File {source_file_path} in directory {dest_file_path} already exists"
                    self.l.error(text)
                    if self.settings["delete_source_after_upload"]:
                        self.l.log(f"Removing {source_file_path}")
                        os.remove(source_file_path)
                        text = f"File {path} removed"
                        self.l.log(text)
                # except yadisk.exceptions.PathExistsError: self.l.log(f'Insufficient Storage')
                except Exception as e:
                    text = f"Error: {e.args[0]}"
                    self.l.error(text)

    # Clean by days_live
    def clean(self, dir):
        try:
            self.y.mkdir(dir)
        except yadisk.exceptions.PathExistsError:
            pass
        dir_content = self.y.listdir(dir)
        duedate = datetime.datetime.utcnow().replace(
            tzinfo=pytz.utc
        ) - datetime.timedelta(days=self.days_l)
        filescount = 0
        for item in dir_content:
            if not item.path:
                raise Exception("Error: Empty path")
            if not item.created:
                raise Exception("Error: Empty created date")
            if item.type == "dir":
                cnt = self.clean(item.path)
                if cnt == 0:
                    self.y.remove(item.path, permanently=True)
                else:
                    filescount += 1
            else:
                if item.created <= duedate:
                    s = format(self.free_space(), ".2f")
                    self.l.log(
                        f"Deleting old file {item.path}. Created date:{item.created}"
                    )
                    self.y.remove(item.path, permanently=True)
                    self.l.log(f"Delete complete. Free space{s} Gb")
                else:
                    filescount += 1
        return filescount

    # Clean oldest files by new file size
    def clean_by_size(self, new_file_size) -> None:
        while (
            new_file_size >= self.free_space()
            and self.folder_size(self.yandex_root) > 0
        ):
            dt, path = self.find_oldest_file(self.yandex_root)
            try:
                self.l.log(f"Removing oldest file: {path} date creation: {dt}")
                self.y.remove(path, permanently=True)
            except Exception as e:
                self.l.log(f"Error: {e.args[0]}")
        s = format(self.free_space(), ".2f")
        self.l.log(f"Delete complete. Free space {s} Gb")

    def folder_size(self, dir_path) -> int:
        dir_content = self.y.listdir(dir_path)
        size: int = 0
        for item in dir_content:
            if item.type == "dir":
                size += self.folder_size(item.path)
            else:
                if item.size:
                    size += item.size
        return size

    def free_space(self) -> float:
        info = self.y.get_disk_info()
        if not info.total_space:
            raise Exception("Error: Empty total_space")
        if not info.used_space:
            raise Exception("Error: Empty used_space")

        fs: float = (info.total_space - info.used_space) / 1024 / 1024 / 1024
        return fs

    def find_oldest_file(self, root) -> tuple:
        dir_content = self.y.listdir(root)
        dt: datetime.datetime = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
        path: str = ""
        for item in dir_content:
            if not item.path:
                raise Exception("Error: Empty path")
            if not item.created:
                raise Exception("Error: Empty created date")
            if item.type == "dir":
                d, p = self.find_oldest_file(item.path)
                if d < dt and not p == "":
                    dt = d
                    path = p
            else:
                if item.created < dt:
                    dt = item.created
                    path = item.path
        return dt, path

    def GetToken(self):
        token = self.settings["oauth_token"]
        if token == "":
            token = self.GetOAuthToken(self.GetOAuthCode())
        return token

    def generate_device_id(self):
        device_id = str(uuid.uuid4())
        self.settings["device_id"] = device_id
        self.settings_obj.save()
        return device_id

    def GetOAuthCode(self):
        authorization_base_url = "https://oauth.yandex.ru/authorize"
        client_id = self.settings["client_id"]
        device_id = self.settings["device_id"]

        if device_id == "":
            device_id = self.generate_device_id()
        auth_url = f"{authorization_base_url}?response_type=code&client_id={client_id}&device_id={device_id}"

        webbrowser.open_new(auth_url)
        print(auth_url)
        print(f"Device Id: {device_id}")
        return input("Yandex code: ")

    def GetOAuthToken(self, code):
        client_id = self.settings["client_id"]
        client_secret = self.settings["client_secret"]
        TOKEN_URL = "https://oauth.yandex.ru/token"
        device_id = self.settings["device_id"]

        if device_id == "":
            device_id = self.generate_device_id()

        # REDIRECT_URI = "https://www.getpostman.com/oauth2/callback"
        # client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
        post_headers = {"Content-Type": "application/x-www-form-urlencoded"}

        post_data = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
        }
        response = requests.post(TOKEN_URL, headers=post_headers, data=post_data)
        token_json = response.json()

        token = str(token_json["access_token"])
        self.settings["oauth_token"] = token
        self.settings_obj.save()
        return token

    def NewToken(self):
        token = self.GetOAuthToken(self.GetOAuthCode())
        self.settings["oauth_token"] = token
        self.settings_obj.save()
        return token


if __name__ == "__main__":
    log = LogWorker()
    ydw = YDWorker(log=log)
