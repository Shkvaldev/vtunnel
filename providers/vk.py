import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from loguru import logger

from . import Provider

class ProviderVK(Provider):
    def __init__(self, token=None, logger = logger):
        self.logger = logger
        self.api = None
        self.token = token

        if not self.token:
            err_msg = """you didn't provide access_token - 
                         Go to https://vkhost.github.io and choose VKAdmin"""
            self.logger.error(err_msg)
            raise ValueError(err_msg)

        try:
            self.auth()
        except Exception as e:
            err_msg = f"Failed to login: {e}"
            self.logger.error(err_msg)
            raise ValueError(err_msg)

    def auth(self):
        self.vk_session = vk_api.VkApi(token=self.token)
        self.api = self.vk_session.get_api()
        self.longpoll = VkLongPoll(self.vk_session)
        self.logger.success("Client initialized successfully")

    def start(self):
        """Entrypoint for dispatcher"""
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                self.logger.debug(f'id{event.user_id}: {event.text}')
