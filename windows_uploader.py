"""
Install service:
python windows_uploader.py install

Start service:
python windows_uploader.py start

Stop service:
python windows_uploader.py stop

Remove service:
python windows_uploader.py remove

Debug service:
python windows_uploader.py debug

dont use poetry virtualenv
install pywin32 and other from pip
"""
# Standard Library
import random
import time
from logging import (
    DEBUG,
    INFO,
)

# My Stuff
from base_windows import SMWinservice
from log_worker import LogWorker
from uploader import main as upload
from yandex_disk import YDWorker


class YandexUploader(SMWinservice):
    _svc_name_ = "YandexUploader"
    _svc_display_name_ = "Yandex Uploader"
    _svc_description_ = "Uploads files to Yandex Disk"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        log = LogWorker(level=INFO)
        yandex_worker = YDWorker(log=log)
        while self.isrunning:
            random.seed()
            upload(log, yandex_worker)
            time.sleep(5)


if __name__ == "__main__":
    YandexUploader.parse_command_line()
