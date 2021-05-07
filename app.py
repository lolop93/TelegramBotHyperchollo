from telethon import TelegramClient, events
from googletrans import Translator
import re


api_id = 5619756
api_hash = 'c1595ea66531639e75a4788d163a0c50'
translator =  Translator()



#client = TelegramClient("name", api_id, api_hash)

'''
async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Hello to myself!')

with client:
    client.loop.run_until_complete(main())
'''
'''
client = TelegramClient('sneakerBot', api_id, api_hash)
client.start()

print(client.get_me().stringify())

client.send_message('Kbs', 'Hello! Talking to you from Telethon')
client.send_file('username', '/home/myself/Pictures/holidays.jpg')

client.download_profile_photo('me')
messages = client.get_messages('Kbs')
messages[0].download_media()

@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey!')
'''

client = TelegramClient('name', api_id, api_hash)

@client.on(events.NewMessage(chats=("@snkrempire", "Group2")))
async def my_event_handler(event):

    print('{}'.format(event))
    if event.media:
        await client.send_file('@SneakersAlertSpainHyperchollo', event.media)

    traduccion = translator.translate(event.text, dest='es')
    print('{}'.format(traduccion.text))

    #myString = event.text
    #url = re.search("(?P<url>https?://[^\s]+)", myString).group("url")
    if event.text:
        await client.send_message('@SneakersAlertSpainHyperchollo', traduccion.text)


client.start()
client.run_until_disconnected()
