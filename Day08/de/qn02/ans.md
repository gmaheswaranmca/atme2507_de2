# Pandas Solutions for prod.csv and supplier.csv

```python
import pandas as pd

# Load data
prod = pd.read_csv('prod.csv')
supplier = pd.read_csv('supplier.csv')

# 1. Fill missing values in the `price` column of prod.csv with the average price.
prod['price'] = prod['price'].fillna(prod['price'].mean())

# 2. Remove duplicate products based on `prod_id`.
prod = prod.drop_duplicates(subset=['prod_id'])

# 3. Convert the `launch_date` column in prod.csv to datetime format.
prod['launch_date'] = pd.to_datetime(prod['launch_date'])

# 4. Drop suppliers from supplier.csv with missing `contact` information.
supplier = supplier.dropna(subset=['contact'])

# 5. Select all products with a price greater than 1000.
products_gt_1000 = prod[prod['price'] > 1000]

# 6. Retrieve all suppliers from USA.
suppliers_usa = supplier[supplier['country'] == 'USA']

# 7. List all products supplied by Supplier A.
supplier_a_id = supplier[supplier['supplier_name'] == 'Supplier A']['supplier_id'].iloc[0]
products_supplier_a = prod[prod['supplier_id'] == supplier_a_id]

# 8. Filter products launched after 2022-01-01.
products_after_2022 = prod[prod['launch_date'] > '2022-01-01']

# 9. Find the average price of products by each supplier.
avg_price_by_supplier = prod.groupby('supplier_id')['price'].mean()

# 10. Count the number of products supplied by each supplier.
count_products_by_supplier = prod.groupby('supplier_id')['prod_id'].count()

# 11. Find the maximum price among all products.
max_price = prod['price'].max()

# 12. List the number of suppliers by country.
suppliers_by_country = supplier.groupby('country')['supplier_id'].count()

# Display results (for demonstration)
print('Products with price > 1000:\n', products_gt_1000)
print('Suppliers from USA:\n', suppliers_usa)
print('Products supplied by Supplier A:\n', products_supplier_a)
print('Products launched after 2022-01-01:\n', products_after_2022)
print('Average price by supplier:\n', avg_price_by_supplier)
print('Count of products by supplier:\n', count_products_by_supplier)
print('Maximum price among all products:', max_price)
print('Number of suppliers by country:\n', suppliers_by_country)
```
