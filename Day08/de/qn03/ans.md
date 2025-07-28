# Pandas Solutions for patient.csv and appointment.csv

```python
import pandas as pd

# Load data
patient = pd.read_csv('patient.csv')
appointment = pd.read_csv('appointment.csv')

# 1. Fill missing values in the `age` column of patient.csv with the average age.
patient['age'] = patient['age'].fillna(patient['age'].mean())

# 2. Remove duplicate patients based on `patient_id`.
patient = patient.drop_duplicates(subset=['patient_id'])

# 3. Convert the `appointment_date` column in appointment.csv to datetime format.
appointment['appointment_date'] = pd.to_datetime(appointment['appointment_date'])

# 4. Drop appointments with missing `doctor` information.
appointment = appointment.dropna(subset=['doctor'])

# 5. Select all patients from Chennai.
patients_chennai = patient[patient['city'] == 'Chennai']

# 6. Retrieve all appointments for Cardiology department.
appointments_cardiology = appointment[appointment['department'] == 'Cardiology']

# 7. List all appointments for patient John Doe.
john_id = patient[patient['patient_name'] == 'John Doe']['patient_id'].iloc[0]
appointments_john = appointment[appointment['patient_id'] == john_id]

# 8. Filter appointments after 2023-07-15.
appointments_after = appointment[appointment['appointment_date'] > '2023-07-15']

# 9. Find the average age of patients by city.
avg_age_by_city = patient.groupby('city')['age'].mean()

# 10. Count the number of appointments for each department.
count_appointments_by_dept = appointment.groupby('department')['appointment_id'].count()

# 11. Find the number of completed appointments for each doctor.
completed_by_doctor = appointment[appointment['status'] == 'Completed'].groupby('doctor')['appointment_id'].count()

# 12. List the number of patients by gender.
patients_by_gender = patient.groupby('gender')['patient_id'].count()

# Display results (for demonstration)
print('Patients from Chennai:\n', patients_chennai)
print('Appointments for Cardiology:\n', appointments_cardiology)
print('Appointments for John Doe:\n', appointments_john)
print('Appointments after 2023-07-15:\n', appointments_after)
print('Average age by city:\n', avg_age_by_city)
print('Appointments by department:\n', count_appointments_by_dept)
print('Completed appointments by doctor:\n', completed_by_doctor)
print('Patients by gender:\n', patients_by_gender)
```
