import json
from loguru import logger


class Mappings:
    def __init__(self, path, logger=logger):
        self.logger = logger
        self.path = path
        self.__data = None

        self.load()

    def load(self, path=None):
        pass
