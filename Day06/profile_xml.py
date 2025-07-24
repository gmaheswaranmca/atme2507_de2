import xml.etree.ElementTree as ET 
def read_employees():
    employees = []
    tree = ET.parse('emp.xml')
    root = tree.getroot()
    emp_nodes = root.findall('employee')
    for emp_node in emp_nodes:
        emp = {
            'name' : emp_node.find('name').text,
            'age' : int(emp_node.find('age').text),
            'job_title' : emp_node.find('job_title').text
        }
        employees.append(emp)
    return employees 

def print_profile(emp):
    print('Name:', emp['name'])
    print('Age:', emp['age'])
    print('Job Title:', emp['job_title'])
    

employees = read_employees()
for emp in employees:
    print_profile(emp)
    print('#' * 50)