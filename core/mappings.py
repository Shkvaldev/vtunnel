import json
from loguru import logger

from bidict import bidict


def keys_to_int(x):
    return {int(k): v for k, v in x.items()}


class Mappings:
    def __init__(self, path, logger=logger):
        self.logger = logger
        self.path = path
        self.__data = None

        self.load()

    def load(self, path=None):
        """Loads mappings from file"""
        if not path:
            path = self.path

        try:
            with open(path, "r") as f:
                self.__data = bidict(json.load(f, object_hook=keys_to_int))
            self.logger.success("Mappings are ready!")
        except Exception as e:
            err_msg = f"Failed to load mappings from file `{self.path}`: {e}"
            self.logger.error(err_msg)
            raise ValueError(err_msg)

    def find_postfix(self, key: int):
        """Finds postfix according to key from mappings"""
        if 0 <= key <= 255:
            return self.__data[key]

        self.logger.error(f"Failed to find postfix by key `{key}`: out of bounds")

    def find_key(self, postfix: str):
        """Finds postfix according to key from mappings"""
        try:
            return self.__data.inverse[postfix]
        except KeyError:
            err_msg = f"Failed to find key by postfix `{postfix}`: there is no such a postfix in mappings!"
            self.logger.error(err_msg)
            raise KeyError(err_msg)
