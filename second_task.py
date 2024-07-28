import requests

params = {'userId': 1}

# Отправка GET-запроса с параметром userId=1
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

# Печать полученных записей
print(response.json())
