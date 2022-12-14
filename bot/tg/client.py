import requests

from bot.tg.dc import GetUpdatesResponse, SendMessageResponse
from todolist import settings


class TgClient:
    def __init__(self, token):
        self.token = token

    def get_url(self, method: str):
        return f"https://api.telegram.org/bot{self.token}/{method}"

    def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdatesResponse:
        url = self.get_url("getUpdates")
        resp = requests.get(url, params={"offset": offset, "timeout": timeout})
        return GetUpdatesResponse.Schema().load(resp.json())

    def send_message(self, chat_id: int, text: str) -> SendMessageResponse:
        url = self.get_url("sendMessage")
        resp = requests.get(url, params={"chat_id": chat_id, "text": text})
        return SendMessageResponse.Schema().load(resp.json())


# cl = TgClient(settings.BOT_TOKEN)
# print(cl.get_updates(offset=0, timeout=60))
#
# cl = TgClient(settings.BOT_TOKEN)
# print(cl.send_message(1044177532, "Привет"))
