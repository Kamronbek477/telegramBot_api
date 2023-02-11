import os 
import requests
from sendMessage import TOKEN

def sendPhoto(chat_id:str,photo:str):
    data = {
        'chat_id':chat_id
    }
    files = {
        "photo":photo
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    r = requests.post(URL, params=data, files=files)
    return r.json()['ok']

    

# photo_url='https://random.dog/2bff25d0-c721-4078-8cc9-f3ce6b464428.jpg'
# photo_id = 'AgACAgIAAxkDAAMgY7evYvSyDJQ8DS-1S5Irjcd9cIgAAoa_MRvjDsFJ4H7lvD-PEXwBAAMCAAN4AAMtBA'
img = open('logo.jpg','rb').read()
print(sendPhoto(5575549228, img))


# send photo with three ways: url, id, file
