import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)
response_data = response.json()
print("Response Data:", response_data)