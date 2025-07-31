import pandas as pd 
from pymongo import MongoClient
import os
#ETL / ELT Pipeline for Employee Data
#Extract - csv to pandas DataFrame
emp_df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'emp.csv'))

#Load - lake pandas DataFrame to MongoDB
client = MongoClient('mongodb+srv://user:pwed@server')
db = client['lake_emp']
collection = db['emps']
collection.delete_many({})
collection.insert_many(emp_df.to_dict('records'))
print('Employees loaded to lake database')

#Transform - MongoDB to pandas DataFrame
emp_df['salary'] = emp_df['salary'].fillna(0)
dept_sal_df = emp_df.groupby('department')['salary'].sum().reset_index()

#Load - warehouse pandas DataFrame to MongoDB
db = client['warehouse_emp']
collection = db['emps']
collection.delete_many({})
collection.insert_many(emp_df.to_dict('records'))
print('Processed Employees loaded to warehouse database')
collection = db['dept_salaries']
collection.delete_many({})
collection.insert_many(dept_sal_df.to_dict('records'))
print('Processed Employees loaded to warehouse database')
