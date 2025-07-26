**Pandas coding questions** based **only on the product and supplier datasets**

---

### 🧹 **Data Cleaning & Preprocessing**

1. Fill missing values in the `price` column of `prod.csv` with the average price.
2. Remove duplicate products based on `prod_id`.
3. Convert the `launch_date` column in `prod.csv` to datetime format.
4. Drop suppliers from `supplier.csv` with missing `contact` information.

---

### 🔍 **Filtering & Conditional Selection**

5. Select all products with a price greater than 1000.
6. Retrieve all suppliers from `USA`.
7. List all products supplied by `Supplier A`.
8. Filter products launched after `2022-01-01`.

---

### 📊 **Aggregation & GroupBy**

9. Find the average price of products by each supplier.
10. Count the number of products supplied by each supplier.
11. Find the maximum price among all products.
12. List the number of suppliers by country.

---

### 📁 **Sample Data: prod.csv**

```csv
prod_id,prod_name,price,launch_date,supplier_id
P001,Laptop,1200,2022-03-15,S001
P002,Smartphone,800,2021-11-10,S002
P003,Tablet,600,2023-01-05,S001
P004,Monitor,300,2022-07-20,S003
P005,Printer,,2022-09-12,S002
P006,Keyboard,50,2021-05-30,S003
P007,Mouse,25,2023-02-18,S001
```

### 📁 **Sample Data: supplier.csv**

```csv
supplier_id,supplier_name,country,contact
S001,Supplier A,USA,alice@example.com
S002,Supplier B,India,
S003,Supplier C,Germany,bob@example.com
S004,Supplier D,USA,charlie@example.com
```
