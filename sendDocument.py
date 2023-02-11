import requests
from sendMessage import TOKEN

def sendDocument(chat_id:str,document:str):
    params = {
        'chat_id':chat_id,
    }
    files = {
        "document":document
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
    r = requests.post(URL, params=params, files=files)
    return r.json()

    
data = open('sendPhoto.py','rb')
print(sendDocument(5575549228, data))

# send photo with three ways: url, id, file
