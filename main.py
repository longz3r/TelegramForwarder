from dotenv import load_dotenv
from telethon import TelegramClient, events
import os
import json

load_dotenv()
with open('config.json', 'r') as file:
    config = json.load(file)

config["forwardFrom"] = list(dict.fromkeys(config["forwardFrom"]))
client = TelegramClient(os.getenv("API_ID"), os.getenv("API_ID"), os.getenv("API_HASH"))

def parseSenderName(sender):
    if hasattr(sender, "first_name") or hasattr(sender, "last_name"):
        return (sender.first_name or "") + " " + (sender.last_name or "") + " - "
    else:
        return ""

async def listChannels(channels):
    for channelId in channels:
        try:
            print(f"{channelId} - {(await client.get_entity(channelId)).title} ")
        except:
            print(f"{channelId} seems to be an invalid one")

async def main():
    await client.start()
    await client.connect()
    print("Connected to telegram")
    await listChannels(config["forwardFrom"])
    await client.run_until_disconnected()
    # await client.forward_messages(target_chat, message_id, source_chat)
    

@client.on(events.NewMessage)
async def handler(event):
    if (not hasattr(event.message.peer_id, "channel_id") or not event.message.peer_id.channel_id in config["forwardFrom"]): return
    sender = await event.get_sender()
    chat = await event.get_chat()
    # print(await client.get_entity(event.message.peer_id.channel_id))
    chat_name = chat.title if chat.title else "Private Chat"
    sender_name = parseSenderName(sender)
    event.message.text += f"\n\n🗣️ {sender_name}{chat_name}"
    print(f"Forwarded message from {sender_name}{chat_name}")
    for target in config["forwardTo"]:
        await client.send_message(target["id"], event.message, reply_to=target["topicId"] if "topicId" in target != None else None)

with client:
    client.loop.run_until_complete(main())

