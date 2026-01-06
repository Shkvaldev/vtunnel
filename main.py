from loguru import logger

from config import Config
from core import WordList, Dialogs, Mappings
from providers import ProviderVK


def main():
    config = Config("config.json")

    # Loading files
    wl = WordList("words.txt")
    dialogs = Dialogs("dialogs.json")
    mappings = Mappings("mappings.json")

    vk = ProviderVK(token=config.providers["vk"][0]["token"])
    vk.start()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.debug("Exitting ...")
