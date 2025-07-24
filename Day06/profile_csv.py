import csv 
def read_employees():
    employees = []
    with open('emp.csv', 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader: # {'name':'Maheswaran', 'age':46, 'job_title':'DETrainer'}
            employees.append(row)
    return employees 

def print_profile(emp):
    print('Name:', emp['name'])
    print('Age:', emp['age'])
    print('Job Title:', emp['job_title'])
    

employees = read_employees()
for emp in employees:
    print_profile(emp)
    print('#' * 50)

