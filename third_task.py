import requests

# Данные для отправки
json = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса с данными
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=json)

# Печать статус-кода ответа
print(response.status_code)

# Печать содержимого ответа
print(response.json())
