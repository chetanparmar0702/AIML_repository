import pandas as pd
import numpy as np
data = {
'Age': [25, 30, np.nan, 35, np.nan],
'Salary': [50000, 54000, 58000, np.nan, 62000],
'Gender': ['Male', 'Female', np.nan, 'Female', 'Male'],
'Department': ['HR', np.nan, 'IT', 'Finance', 'IT']
}

df=pd.DataFrame(data)
print("\nCount of Missing Values in Each Column:\n", df.isnull().sum())

df_dropped = df.dropna()
print("\nDataFrame after Dropping Rows with Missing Values:\n", df_dropped)
age_mean = df['Age'].mean()
df.fillna({'Age': age_mean}, inplace=True)
# df['Age'].fillna(df['Age'].mean(), inplace=True)
print("\nDataFrame after Filling 'Age' with Mean:\n", df)

salary_mean = df['Salary'].mean()
df.fillna({'Salary': salary_mean}, inplace=True)
print("\nDataFrame after Filling 'Salary' with Mean:\n", df)

df['Age'].fillna(df['Age'].mode()[0], inplace=True)

df['Salary'] = df['Salary'].interpolate()
print("\nDataFrame after Interpolating 'Salary':\n", df)

df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
print("\nDataFrame after Filling 'Gender' with Mode:\n", df)

df['Department'].fillna('Unknown', inplace=True)
print("\nDataFrame after Filling 'Department' with 'Unknown':\n", df)

df['Department'].fillna(method='ffill', inplace=True)
print("\nDataFrame after Forward Filling 'Department':\n", df)

print("\nFinal DataFrame after Handling Missing Values:\n", df)