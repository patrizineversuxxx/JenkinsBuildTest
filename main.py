import requests


url = "https://www.list.am/ru/"
response = requests.get(url=url)
response_code = response.status_code

print(response)
