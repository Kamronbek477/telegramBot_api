import os
import requests

TOKEN = '5661659754:AAHjcXFhVC9UdI0Q83YBMReNptJXBXFFESs'

def sendMessage(chat_id:str, text:str):
    button1 = {'text':'Dog'}
    button2 = {'text':'Cat'}

    keyboard = [[button1, button2]]

    reply_markup = {'keyboard':keyboard}

    payload = {
        'chat_id':chat_id,
        'text':text,
        'reply_markup':reply_markup
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    response = requests.post(URL, json=payload)
    return response.json()

chat_id = 5575549228
text = "HELLO"
print(sendMessage(chat_id, text))
    
