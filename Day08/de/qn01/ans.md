**Pandas code answers for Questions** on the `employees` dataset:

---

### 🧹 Data Cleaning & Preprocessing

**Q1.** Fill missing values in `salary` with average:

```python
df['salary'].fillna(df['salary'].mean())
```

**Q2.** Drop rows with any missing values:

```python
df.dropna()
```

**Q3.** Remove duplicate rows:

```python
df.drop_duplicates()
```

**Q4.** Convert `join_date` to datetime:

```python
df['join_date'] = pd.to_datetime(df['join_date'])
```

**Q5.** Create `join_year` and `join_month`:

```python
df['join_year'] = df['join_date'].dt.year
df['join_month'] = df['join_date'].dt.month
```

---

### 🔍 Filtering & Conditional Selection

**Q6.** IT employees with salary > 75000:

```python
df[(df['department'] == 'IT') & (df['salary'] > 75000)]
```

**Q7.** Employees who joined before 2020:

```python
df[df['join_date'] < '2020-01-01']
```

**Q8.** Top 5 performers:

```python
df.sort_values(by='performance_score', ascending=False).head(5)
```

**Q9.** Marketing employees in Boston:

```python
df[(df['department'] == 'Marketing') & (df['city'] == 'Boston')]
```

**Q10.** Rows where salary is missing:

```python
df[df['salary'].isna()]
```

---

### 📊 Aggregation & GroupBy

**Q11.** Average salary by department:

```python
df.groupby('department')['salary'].mean().reset_index()
```

**Q12.** Number of employees per city:

```python
df['city'].value_counts().reset_index().rename(columns={'index': 'city', 'city': 'employee_count'})
```

**Q13.** Max performance score per department:

```python
df.groupby('department')['performance_score'].max().reset_index()
```

**Q14.** Total salary in Finance department:

```python
df[df['department'] == 'Finance']['salary'].sum()
```

**Q15.** Number of employees joined per year:

```python
df['join_year'].value_counts().sort_index().reset_index().rename(
    columns={'index': 'join_year', 'join_year': 'employee_count'})
```

### 🔗 Joins and Merging (Assume `departments` DataFrame with `department_id`, `department_name`)

**Q16.** Merge employee data with department names:

```python
merged_df = df.merge(departments_df, on='department', how='left')
```

**Q17.** Employees whose department name is 'Marketing':

```python
merged_df[merged_df['department'] == 'Marketing']
```

---

### 🪟 Window Functions (Using `groupby` + `rank`, `cumsum`, etc.)

**Q18.** Rank employees by performance within department:

```python
df['rank'] = df.groupby('department')['performance_score'].rank(ascending=False)
```

**Q19.** Cumulative salary by department:

```python
df['cumulative_salary'] = df.sort_values('join_date') \
    .groupby('department')['salary'].cumsum()
```

**Q20.** Find employees with highest salary in each department:

```python
top_earners = df.loc[df.groupby('department')['salary'].idxmax()]
```

---

### 🔄 Pivoting & Reshaping

**Q21.** Pivot table: avg salary by city and department:

```python
pd.pivot_table(df, values='salary', index='city', columns='department', aggfunc='mean')
```

**Q22.** Melt the DataFrame to long format:

```python
pd.melt(df, id_vars=['emp_id', 'department'], value_vars=['salary', 'performance_score'])
```

---

### 📅 Date & Time Operations

**Q23.** Tenure (in days) for each employee:

```python
df['tenure_days'] = (pd.to_datetime('today') - df['join_date']).dt.days
```

**Q24.** Number of employees joined in each quarter:

```python
df['join_quarter'] = df['join_date'].dt.to_period('Q')
df['join_quarter'].value_counts().sort_index()
```

**Q25.** Employees joined in last 6/50 months:

```python
fifty_months_ago = pd.to_datetime('today') - pd.DateOffset(months=50)
df[df['join_date'] >= fifty_months_ago]
```

**Q26.** Create `years_with_company`:

```python
df['years_with_company'] = (pd.to_datetime('today') - df['join_date']).dt.days // 365
```

**Q27.** Filter employees who completed 5+ years:

```python
df[df['years_with_company'] >= 5]
```

