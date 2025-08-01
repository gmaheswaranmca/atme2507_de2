import pandas as pd 
from pymongo import MongoClient
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('etl_pipeline.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

#ETL / ELT Pipeline for Employee Data
logger.info("Starting ETL pipeline for Employee Data")

try:
    #Extract - csv to pandas DataFrame
    logger.info("Starting data extraction from CSV file")
    emp_df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'emp.csv'))
    logger.info(f"Successfully extracted {len(emp_df)} records from emp.csv")
    logger.debug(f"DataFrame shape: {emp_df.shape}")
    logger.debug(f"DataFrame columns: {emp_df.columns.tolist()}")
except Exception as e:
    logger.error(f"Failed to extract data from CSV: {str(e)}")
    raise

try:
    #Load - lake pandas DataFrame to MongoDB
    logger.info("Starting data load to lake database")
    client = MongoClient('mongodb+srv://mahesh:12345@cluster0.wkvfjw4.mongodb.net')
    logger.info("Successfully connected to MongoDB")
    
    db = client['lake_emp']
    collection = db['emps']
    logger.info("Clearing existing data from lake database")
    delete_result = collection.delete_many({})
    logger.info(f"Deleted {delete_result.deleted_count} existing records from lake database")
    
    collection.insert_many(emp_df.to_dict('records'))
    logger.info(f'Successfully loaded {len(emp_df)} employees to lake database')
except Exception as e:
    logger.error(f"Failed to load data to lake database: {str(e)}")
    raise

try:
    #Transform - MongoDB to pandas DataFrame
    logger.info("Starting data transformation")
    logger.debug(f"Original salary column stats: {emp_df['salary'].describe()}")
    
    # Check for null values before transformation
    null_count = emp_df['salary'].isnull().sum()
    if null_count > 0:
        logger.warning(f"Found {null_count} null values in salary column, filling with 0")
    
    emp_df['salary'] = emp_df['salary'].fillna(0)
    logger.info("Successfully filled null salary values with 0")
    
    dept_sal_df = emp_df.groupby('department')['salary'].sum().reset_index()
    logger.info(f"Successfully aggregated salary by department: {len(dept_sal_df)} departments")
    logger.debug(f"Department salary summary: {dept_sal_df.to_dict('records')}")
except Exception as e:
    logger.error(f"Failed during data transformation: {str(e)}")
    raise

#Load - warehouse pandas DataFrame to MongoDB
db = client['warehouse_emp']
collection = db['emps']
collection.delete_many({})
collection.insert_many(emp_df.to_dict('records'))
print('Processed Employees loaded to warehouse database')
collection = db['dept_salaries']
collection.delete_many({})
collection.insert_many(dept_sal_df.to_dict('records'))
print('Processed Dept Salaries loaded to warehouse database')
