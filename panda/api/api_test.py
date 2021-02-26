import requests

api = 'http://127.0.0.1:5000/'
r = requests.get(api + '/api/v1/model/demographic', {'id_person': "3"})
print(r.text)


r = requests.get(api + '/api/v1/model/recommendation', {'id_person': '0', 'limit': '3'})
print(r.text)