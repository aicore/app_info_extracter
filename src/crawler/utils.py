import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
import yaml
import os
import shutil


class Utils:
    @staticmethod
    def print_json(json_object):
        """This method will do json pretty print"""
        json_str = json.dumps(json_object,
                              indent=2,
                              sort_keys=True,
                              default=str)
        print(highlight(json_str, JsonLexer(), TerminalFormatter()))

    @staticmethod
    def read_yaml_config_file(config_file):
        with open(config_file, 'r') as file:
            doc = yaml.load(file, Loader=yaml.FullLoader)
            return doc

    @staticmethod
    def create_directory_if_not_exit(dir_name):
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

    @staticmethod
    def get_cwd():
        return os.getcwd()

    @staticmethod
    def move_file_to_folder(file_name, dest_folder):
        shutil.move(file_name, dest_folder)

    @staticmethod
    def is_file_present(file):
        return os.path.isfile(file)
