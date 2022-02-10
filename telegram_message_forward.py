import asyncio
from telethon.errors import SessionPasswordNeededError
from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel


API_ID = ""  # personal api i
API_HASH = ""  # personal api hash key
PHONE = ""  # number and username not required, you will be promted automatically to enter it via terminal
USERNAME = ""

# CHANNELS_ID_LIST


def main():
    with TelegramClient("name", API_ID, API_HASH) as client:
        # replace the channel id with a list of channel ids to hear from
        @client.on(events.newmessage.NewMessage([1717894590]))
        async def handler(event):
            print(event.message.message)
            # id of the channel to forward messages to
            await event.forward_to(1696214934)

        client.run_until_disconnected()


if __name__ == "__main__":
    main()
