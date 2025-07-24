import json 
def read_employees():    
    with open('emp.json', 'r', encoding='utf-8') as file:
        employees = json.load(file)
    return employees 

def print_profile(emp):
    print('Name:', emp['name'])
    print('Age:', emp['age'])
    print('Job Title:', emp['job_title'])
    

employees = read_employees()
for emp in employees:
    print_profile(emp)
    print('#' * 50)

