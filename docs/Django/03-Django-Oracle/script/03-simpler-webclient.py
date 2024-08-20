import requests
result = requests.get("http://127.0.0.1:8888/remeo.txt")
print(result.text)