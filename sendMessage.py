import os
import requests

TOKEN = '5661659754:AAHjcXFhVC9UdI0Q83YBMReNptJXBXFFESs'


def sendMessage(chat_id:str, text:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id':chat_id, 
        'text':text,
        'parse_mode':'MarkdownV2'}
    response = requests.post(url=URL, data=payload)
    return response.json()
    
print(sendMessage(5575549228, "*Hello*  _Hello_"))