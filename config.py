import json
from loguru import logger


class Config:
    def __init__(self, config_path, logger=logger):
        self.config_path = config_path
        self.logger = logger

        self.providers = None

        self.load()

    def load(self):
        try:
            with open(self.config_path, "r") as conf:
                ctx = json.loads(conf.read())
                # Assigning properties

                # Providers info
                if not "providers" in ctx:
                    raise ValueError("there is no provider data")

                self.providers = ctx["providers"]

        except Exception as e:
            self.logger.error(f"Failed to load config: {e}")
            raise e

    def save(self):
        try:
            with open(self.config_path, "w") as conf:
                data = {}
                conf.write(json.dumps(data, indent=4))
        except Exception as e:
            self.logger.error(f"Failed to save config data: {e}")
            raise e
