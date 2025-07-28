**Pandas coding questions** based **only on the employee dataset**

---

### 🧹 **Data Cleaning & Preprocessing**

1. Fill the missing values in the `salary` column with the average salary.
2. Drop rows that have any missing values.
3. Remove duplicate rows from the dataset.
4. Convert the `join_date` column to datetime format.
5. Create new columns `join_year` and `join_month` from the `join_date` column.

---

### 🔍 **Filtering & Conditional Selection**

6. Select all employees from the `IT` department earning more than 75000.
7. Retrieve all employees who joined before `2020-01-01`.
8. Get the top 5 employees with the highest `performance_score`.
9. List all employees from `Boston` in the `Marketing` department.
10. Filter rows where the `salary` is missing.

---

### 📊 **Aggregation & GroupBy**

11. Find the average salary by each department.
12. Count the number of employees in each city.
13. Find the maximum performance score in each department.
14. Calculate the total salary paid to employees in the `Finance` department.
15. Find the number of employees who joined each year.

---

### 🔗 **Joins (Assume departments.csv is available)**

16. Join the employee dataset with `departments.csv` on the `department` column using a left join.
17. After joining, display employees along with their respective managers.
18. List employees whose manager is `Clara`.

---

### 🔁 **Window Functions & Time-based Analysis**

19. Create a column that contains the previous employee’s `salary` in the dataset.
20. Find the difference in salary compared to the previous row.
21. Rank employees by `performance_score` within each department.

---

### 🔀 **Pivoting & Reshaping**

22. Create a pivot table to show average salary per department per city.
23. Melt the DataFrame to convert `salary` and `performance_score` into value columns.
24. Unstack the count of employees per department and city.

---

### ⏱ **Datetime & Resampling**

25. Count the number of employees who joined each month.
26. Find the earliest join date for each department.
27. Resample the number of joinings per year using `join_date`.
