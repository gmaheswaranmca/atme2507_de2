import requests 
base = 'https://jsonplaceholder.typicode.com/'
#all todos 
def create(title, completed):
    todo = {"title" : title, "completed" : completed, "userId": 1}
    url = f'{base}/todos'
    response = requests.post(url, json = todo)
    savedTodo = response.json()
    print(savedTodo)

def read_all_todos():
    url = f'{base}/todos'
    response = requests.get(url)
    todos = response.json()
    print('All the todos:\n',todos)
    print()

def read_by_id(id):
    url = f'{base}/todos/{id}'
    response = requests.get(url)
    todo = response.json()
    print('Todo:\n',todo)
    print()
    return todo 

def update(id, title, completed):
    oldTodo = read_by_id(id)
    oldTodo["title"] = title 
    oldTodo["completed"] = completed
    url = f'{base}/todos/{id}'
    response = requests.put(url, oldTodo)
    newTodo = response.json()
    print(newTodo)

def delete(id):
    url = f'{base}/todos/{id}'
    response = requests.delete(url)
    data = response.json()
    if response.status_code == 200:
        print('Todo is deleted successfully')
    print(data)
#read_all_todos()
#read_by_id(13)
#create('Mongo DB Installation and Setup', False)
#update(13,"I am chaning the title", True)
delete(13)




