from loguru import logger

from config import Config
from core import WordList
from providers import ProviderVK


def main():
    config = Config("config.json")
    wl = WordList("words.txt")

    vk = ProviderVK(token=config.providers["vk"][0]["token"])
    vk.start()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.debug("Exitting ...")
