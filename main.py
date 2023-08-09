import requests


url = "https://www.list.am/ru/"
request = requests.get(url=url)
request_code = request.status_code

print(request_code)
