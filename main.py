import requests

r = requests.get('https://random.dog/woof.json')

print(r.json())