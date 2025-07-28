# Pandas: Comprehensive Notes

## 1. Introduction to Pandas

- **Pandas** is a powerful open-source Python library for data analysis and manipulation.
- It provides fast, flexible data structures (Series and DataFrame) designed to work with structured data.
- Commonly used in data science, analytics, ETL pipelines, and machine learning workflows.

## 2. Core Data Structures

### a. Series
- 1-dimensional labeled array (like a column in Excel or a single list with labels).
- Can hold any data type (integers, strings, floats, etc.).

```python
import pandas as pd
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
```

### b. DataFrame
- 2-dimensional labeled data structure (like a spreadsheet or SQL table).
- Consists of rows and columns, each with labels.

```python
data = {'name': ['Alice', 'Bob'], 'age': [25, 30]}
df = pd.DataFrame(data)
print(df)
```

## 3. Reading and Writing Data

### a. Reading CSV
```python
df = pd.read_csv('data.csv')
```
### b. Reading Excel
```python
df = pd.read_excel('data.xlsx')
```
### c. Reading JSON
```python
df = pd.read_json('data.json')
```
### d. Writing Data
```python
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
df.to_json('output.json')
```

## 4. Exploring Data

```python
df.head()        # First 5 rows
df.tail()        # Last 5 rows
df.info()        # Data types and non-null counts
df.describe()    # Summary statistics for numeric columns
df.columns       # List of column names
df.shape         # (rows, columns)
```

## 5. Selecting Data

### a. Selecting Columns
```python
df['age']            # Single column (Series)
df[['name', 'age']]  # Multiple columns (DataFrame)
```
### b. Selecting Rows
```python
df.loc[2]            # By label/index
df.iloc[0:3]         # By integer position
```
### c. Conditional Selection
```python
df[df['age'] > 25]
```

## 6. Data Cleaning

### a. Handling Missing Values
```python
df.isnull().sum()            # Count missing values
df.dropna()                  # Drop rows with missing values
df.fillna(0)                 # Fill missing values with 0
df['age'].fillna(df['age'].mean())  # Fill with mean
```
### b. Removing Duplicates
```python
df.drop_duplicates()
```
### c. Data Type Conversion
```python
df['age'] = df['age'].astype(int)
df['date'] = pd.to_datetime(df['date'])
```

## 7. Data Transformation

### a. Creating New Columns
```python
df['age_in_5_years'] = df['age'] + 5
```
### b. Applying Functions
```python
df['salary_bracket'] = df['salary'].apply(lambda x: 'High' if x > 50000 else 'Low')
```
### c. String Operations
```python
df['name'] = df['name'].str.upper()
df['email_domain'] = df['email'].str.split('@').str[1]
```

## 8. Sorting and Filtering

```python
df.sort_values('age', ascending=False)
df[df['city'] == 'Chennai']
```

## 9. GroupBy and Aggregation

### a. GroupBy
```python
df.groupby('department')['salary'].mean()
df.groupby(['city', 'gender'])['age'].count()
```
### b. Aggregation Functions
- `sum()`, `mean()`, `count()`, `min()`, `max()`, `median()`, `std()`

## 10. Merging and Joining DataFrames

```python
pd.merge(df1, df2, on='id', how='inner')
pd.concat([df1, df2], axis=0)  # Stack rows
pd.concat([df1, df2], axis=1)  # Stack columns
```

## 11. Pivot Tables and Crosstab

```python
pd.pivot_table(df, values='salary', index='department', columns='gender', aggfunc='mean')
pd.crosstab(df['city'], df['gender'])
```

## 12. Exporting and Saving Data

```python
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
```

## 13. Visualization with Pandas

```python
df['age'].plot(kind='hist')
df.groupby('city')['salary'].mean().plot(kind='bar')
import matplotlib.pyplot as plt
plt.show()
```

## 14. Useful Tips

- Use `copy()` to avoid SettingWithCopyWarning: `df2 = df1.copy()`
- Use `inplace=True` for operations that modify the DataFrame directly.
- Use `query()` for complex filtering: `df.query('age > 30 and city == "Chennai"')`
- Use `value_counts()` for frequency counts: `df['city'].value_counts()`

## 15. References

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
- [Pandas Tutorials - DataCamp](https://www.datacamp.com/tutorial/pandas-tutorial-dataframe-python)
