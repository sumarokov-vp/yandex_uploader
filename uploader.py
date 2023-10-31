# Standard Library
import json
import os
import sys
import time
from logging import (
    DEBUG,
    INFO,
)

# My Stuff
from log_worker import LogWorker
from yandex_disk import YDWorker

SETTINGS = os.path.join(os.path.dirname(__file__), "settings.json")


def main(logger=None):
    # load local folders list from settings.json
    with open(SETTINGS, "r") as f:
        settings = json.load(f)
    folders = settings["yandex"]["local_folders"]

    # # upload files from local folders to Yandex.Disk
    logger.debug("Creating Yandex.Disk worker")
    yandex_worker = YDWorker(logger=logger)
    logger.debug("Yandex.Disk worker created")
    for folder in folders:
        full_path = os.path.join(os.path.dirname(__file__), folder)
        yandex_worker.recursive_upload(full_path)


def loop():
    log = LogWorker(DEBUG)
    while True:
        main(log)
        time.sleep(10)


if __name__ == "__main__":
    # repeat uploading every 5 minutes
    try:
        loop()
    except KeyboardInterrupt:
        sys.exit()
