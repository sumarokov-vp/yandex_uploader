# Standard Library
import json
import os


class Settings:
    def __init__(self, file_name="settings.json"):
        # add current directory to file name
        file_name = os.path.join(os.path.dirname(__file__), file_name)
        self.file_name = file_name
        # if file does not exist, create it
        if not os.path.isfile(file_name):
            with open(file_name, "w") as outfile:
                json.dump({}, outfile)
        # load data from file
        # if file is empty, create empty dict
        # else load data from file

        if os.stat(file_name).st_size == 0:
            self.data = {}
        else:
            with open(file_name) as json_file:
                self.data = json.load(json_file)

    def save(self):
        with open(self.file_name, "w") as outfile:
            json.dump(self.data, outfile, indent=4, sort_keys=True)
