import pandas as pd
import numpy as np

file_path = 'Messy_Employee_dataset.csv'
df = pd.read_csv(file_path, na_values=['N/A', 'NaN', 'null'])

print(df.info())

df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')

str_columns = ['First_Name', 'Last_Name', 'Email', 'Department_Region', 'Status', 'Performance_Score']
for col in str_columns:
    df[col] = df[col].astype(str).str.strip()

df[['Department', 'Region']] = df['Department_Region'].str.split('-', expand=True)
df['Phone'] = df['Phone'].abs()
df['Age'] = df['Age'].fillna(df['Age'].median()).astype(int)
df['Salary'] = df['Salary'].fillna(df['Salary'].median()).round(2)

final_columns = [
    'Employee_ID', 'First_Name', 'Last_Name', 'Age', 'Department', 
    'Region', 'Status', 'Join_Date', 'Salary', 'Email', 'Phone', 
    'Performance_Score', 'Remote_Work'
]
df_cleaned = df[final_columns]

print("Missing Values Audit:\n", df_cleaned.isnull().sum())
print("\nData Types Audit:\n", df_cleaned.dtypes)

# ---  EXPORT ---
df_cleaned.to_csv('Cleaned_Employee_Dataset.csv', index=False)
print("\nFile successfully exported to 'Cleaned_Employee_Dataset.csv'")