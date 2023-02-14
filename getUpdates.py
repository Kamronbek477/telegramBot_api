import requests
from sendMessage import sendMessage
TOKEN = '5661659754:AAHjcXFhVC9UdI0Q83YBMReNptJXBXFFESs'

def get_updates():
    BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url=BASE_URL)
    return response.json()['result']

def last_update(result):

    data = result[-1]
    message = data.get('message')
    chat_id = message.get('chat').get('id')
    update_id = data.get('update_id')
    if message.get('text', False):
        keyword = 'text'
        return update_id, chat_id, message.get('text'), keyword

    elif message.get('photo', False):
        keyword = 'photo'
        return update_id, chat_id, message.get('photo')[0]['file_id'], keyword

data = last_update(get_updates())

update_id, chat_id, message, keyword = data

if keyword == 'text':
    sendMessage(chat_id, message)