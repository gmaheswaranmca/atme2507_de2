from flask import Flask, jsonify

app = Flask(__name__)

# Enable CORS for the Flask app 
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # all routes will have CORS enabled

# In-memory employee store for demo
employees = [
    {'emp_id': 101, 'name': 'Alice', 'department': 'IT', 'city': 'New York', 'salary': 72000.0, 'join_date': '2019-06-15', 'performance_score': 88}, 
    {'emp_id': 102, 'name': 'Bob', 'department': 'HR', 'city': 'Boston', 'salary': 58000.0, 'join_date': '2020-08-01', 'performance_score': 77}, 
    {'emp_id': 103, 'name': 'Charlie', 'department': 'Finance', 'city': 'Chicago', 'salary': 67000.0, 'join_date': '2018-01-10', 'performance_score': 91}, 
    {'emp_id': 104, 'name': 'David', 'department': 'IT', 'city': 'Boston', 'salary': 75000.0, 'join_date': '2017-03-25', 'performance_score': 85}, 
    {'emp_id': 105, 'name': 'Eve', 'department': 'Finance', 'city': 'New York', 'salary': 69000.0, 'join_date': '2021-07-11', 'performance_score': 92}, 
    {'emp_id': 106, 'name': 'Frank', 'department': 'IT', 'city': 'Chicago', 'salary': None, 'join_date': '2019-11-04', 'performance_score': 80}, 
    {'emp_id': 107, 'name': 'Grace', 'department': 'Marketing', 'city': 'San Francisco', 'salary': 61000.0, 'join_date': '2020-12-23', 'performance_score': 84}, 
    {'emp_id': 108, 'name': 'Heidi', 'department': 'IT', 'city': 'San Francisco', 'salary': 74000.0, 'join_date': '2016-10-18', 'performance_score': 88}, 
    {'emp_id': 109, 'name': 'Ivy', 'department': 'Marketing', 'city': 'Boston', 'salary': 60000.0, 'join_date': '2018-05-29', 'performance_score': 76}, 
    {'emp_id': 110, 'name': 'John', 'department': 'HR', 'city': 'New York', 'salary': 59000.0, 'join_date': '2021-03-13', 'performance_score': 79}, 
    {'emp_id': 111, 'name': 'Kate', 'department': 'Finance', 'city': 'Chicago', 'salary': 73000.0, 'join_date': '2019-02-20', 'performance_score': 89}, 
    {'emp_id': 112, 'name': 'Leo', 'department': 'IT', 'city': 'Boston', 'salary': 77000.0, 'join_date': '2022-01-01', 'performance_score': 95}, 
    {'emp_id': 113, 'name': 'Mike', 'department': 'Marketing', 'city': 'New York', 'salary': 61000.0, 'join_date': '2017-09-15', 'performance_score': 82}, 
    {'emp_id': 114, 'name': 'Nina', 'department': 'HR', 'city': 'San Francisco', 'salary': 62000.0, 'join_date': '2016-06-22', 'performance_score': 80}, 
    {'emp_id': 115, 'name': 'Owen', 'department': 'Finance', 'city': 'Chicago', 'salary': 68000.0, 'join_date': '2018-12-19', 'performance_score': 73}, 
    {'emp_id': 116, 'name': 'Paul', 'department': 'IT', 'city': 'New York', 'salary': 76000.0, 'join_date': '2021-10-05', 'performance_score': 90}, 
    {'emp_id': 117, 'name': 'Quinn', 'department': 'Marketing', 'city': 'Boston', 'salary': None, 'join_date': '2019-05-30', 'performance_score': 85}, 
    {'emp_id': 118, 'name': 'Rachel', 'department': 'Finance', 'city': 'San Francisco', 'salary': 71000.0, 'join_date': '2020-04-17', 'performance_score': 88}, 
    {'emp_id': 119, 'name': 'Steve', 'department': 'HR', 'city': 'Chicago', 'salary': 60000.0, 'join_date': '2021-02-10', 'performance_score': 81}, 
    {'emp_id': 120, 'name': 'Tina', 'department': 'IT', 'city': 'San Francisco', 'salary': 72000.0, 'join_date': '2018-08-28', 'performance_score': 87}
]

# Read all
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

import os
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)