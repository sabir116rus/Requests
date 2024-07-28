import requests

params = {'q': 'html'}

# Отправка GET-запроса к API GitHub для поиска репозиториев с кодом html
response = requests.get('https://api.github.com/search/repositories', params=params)

# Печать статус-кода ответа
print(response.status_code)

# Печать содержимого ответа в формате JSON
print(response.json())
