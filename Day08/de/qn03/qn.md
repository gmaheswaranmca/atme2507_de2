**Pandas coding questions** based **only on the patient and appointment datasets**

---

### 🧹 **Data Cleaning & Preprocessing**

1. Fill missing values in the `age` column of `patient.csv` with the average age.
2. Remove duplicate patients based on `patient_id`.
3. Convert the `appointment_date` column in `appointment.csv` to datetime format.
4. Drop appointments with missing `doctor` information.

---

### 🔍 **Filtering & Conditional Selection**

5. Select all patients from `Chennai`.
6. Retrieve all appointments for `Cardiology` department.
7. List all appointments for patient `John Doe`.
8. Filter appointments after `2023-07-15`.

---

### 📊 **Aggregation & GroupBy**

9. Find the average age of patients by city.
10. Count the number of appointments for each department.
11. Find the number of completed appointments for each doctor.
12. List the number of patients by gender.

---

### 📁 **Sample Data: patient.csv**

```csv
patient_id,patient_name,age,gender,city
P001,John Doe,35,M,Chennai
P002,Jane Smith,28,F,Bangalore
P003,Arun Kumar,42,M,Hyderabad
P004,Meena Iyer,30,F,Chennai
P005,Ravi Patel,50,M,Mumbai
P006,Anita Desai,25,F,Bangalore
P007,Sunil Rao,38,M,Hyderabad
```

### 📁 **Sample Data: appointment.csv**

```csv
appointment_id,patient_id,doctor,appointment_date,department,status
A001,P001,Dr. Rao,2023-07-10,Cardiology,Completed
A002,P002,Dr. Mehta,2023-07-12,Neurology,Cancelled
A003,P003,Dr. Singh,2023-07-15,Orthopedics,Completed
A004,P001,Dr. Rao,2023-08-01,Cardiology,Pending
A005,P004,Dr. Gupta,2023-07-20,Dermatology,Completed
A006,P005,Dr. Mehta,2023-07-22,Neurology,Completed
A007,P006,Dr. Singh,2023-08-02,Orthopedics,Pending
A008,P007,Dr. Gupta,2023-08-05,Dermatology,Completed
```
