# /_temp_/config.py
# Contains Config class

# Importing modules
import os


class Config:
    @staticmethod
    def get_entry_value(entry_name):
        entry_name = str(entry_name)

        config_txt_path = os.path.join(os.getcwd(), "_temp_", "config.txt")

        with open(config_txt_path, "r") as config_txt_file:
            config_lines = config_txt_file.readlines()

        for line in config_lines:

            if entry_name in line:
                return line[line.find(":")+1:].replace("\n", "")
    @staticmethod
    def get_active_mods_list():
        pass  # TODO: Stub
