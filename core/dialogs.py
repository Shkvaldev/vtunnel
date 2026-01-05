import json
from loguru import logger


class Dialogs:
    def __init__(self, path, logger=logger):
        self.logger = logger
        self.path = path
        self.__data = None

        self.load()

    def load(self, path=None):
        """Loads dialogs from file"""
        if not path:
            path = self.path

        try:
            with open(path, "r") as f:
                self.__data = json.load(f)
            self.logger.success("Dialogs are ready!")
        except Exception as e:
            err_msg = f"Failed to load dialogs from file `{self.path}`: {e}"
            self.logger.error(err_msg)
            raise ValueError(err_msg)
