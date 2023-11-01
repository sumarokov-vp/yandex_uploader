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


def main(logger: LogWorker, yandex_worker: YDWorker):
    # load local folders list from settings.json
    with open(SETTINGS, "r") as f:
        settings = json.load(f)
    folders = settings["yandex"]["local_folders"]

    # # upload files from local folders to Yandex.Disk
    logger.debug(f"Uploading files from {folders}")
    for folder in folders:
        # full_path = os.path.join(os.path.dirname(__file__), folder)
        yandex_worker.recursive_upload(folder)


def loop(log_level: int = INFO):
    log = LogWorker(level=log_level)
    yandex_worker = YDWorker(log=log)
    while True:
        main(log, yandex_worker)
        time.sleep(10)


if __name__ == "__main__":
    # set log level from command line
    if len(sys.argv) < 2:
        log_level = INFO
    else:
        if sys.argv[1].lower() == "debug":
            log_level = DEBUG
    try:
        loop(log_level)
    except KeyboardInterrupt:
        sys.exit()
