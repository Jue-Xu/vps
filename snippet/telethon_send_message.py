from telethon import TelegramClient, events, sync
import time

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 
api_hash = ''

client = TelegramClient('session_name', api_id, api_hash)
client.start()

print(client.get_me().stringify())

group_links = ['https://t.me/NakoNetwork','https://t.me/Singularity_Emby_Group']

for link in group_links:
    entity=client.get_entity(link)
    client.send_message(entity=entity, message='签到')
    time.sleep(10)
    #client.send_message('arthurmerlin', '签到')
