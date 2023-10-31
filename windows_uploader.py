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

# My Stuff
from base_windows import SMWinservice
from uploader import main as upload


class YandexUploader(SMWinservice):
    _svc_name_ = "YandexUploader"
    _svc_display_name_ = "Yandex Uploader"
    _svc_description_ = "Uploads files to Yandex Disk"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            random.seed()
            upload()
            time.sleep(5)


if __name__ == "__main__":
    YandexUploader.parse_command_line()
