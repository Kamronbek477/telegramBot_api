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

def sendContact(chat_id, number, first_name, last_name="No Name"):
    params = {
        'chat_id':chat_id,
        'phone_number':number,
        'first_name':first_name
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendContact'
    r = requests.post(URL, params=params)
    return r.json() 

    
def sendDice(chat_id, emoji):
    params = {
        'chat_id':chat_id,
        'emoji':emoji,
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendDice'
    r = requests.post(URL, params=params)
    return r.json() 

data = open('sendPhoto.py','rb')
print(sendDice(5575549228, emoji='🎰'))

# send photo with three ways: url, id, file
