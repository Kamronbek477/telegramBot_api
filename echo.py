from getUpdates import get_updates
from sendMessage import sendMessage
from time import sleep

last_update_id = -1

while True:
    data = get_updates()
    update_id = data[-1]['update_id']
    chat_id = data[-1]['message']['chat']['id']
    text = data[-1]['message']['text']

    print(text, chat_id)
    if update_id != last_update_id:
        sendMessage(chat_id, "**Hello** | Hello")
        last_update_id = update_id
    
    sleep(2)