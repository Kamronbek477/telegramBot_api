import requests

TOKEN = '5661659754:AAHjcXFhVC9UdI0Q83YBMReNptJXBXFFESs'

def get_updates():
    BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url=BASE_URL)
    return response.json()['result']