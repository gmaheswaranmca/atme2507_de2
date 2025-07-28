import requests 
base = 'https://jsonplaceholder.typicode.com/'
#all todos 
url = f'{base}/todos'
response = requests.get(url)
todos = response.json()
print(todos)

