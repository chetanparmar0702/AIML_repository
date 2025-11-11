import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'] * 4,
    'Age': [24, 27, 22, 25, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco'] * 4
}

#df = pd.DataFrame(data)
df = pd.read_csv('employees.csv')
print(df.head())
# Bar Plot: Average Sales by Region
plt.figure(figsize=(8, 5))
sns.barplot(x='Name', y='Age', data=df)
plt.title('Bar Plot: Average Age')
plt.ylabel('Age')
plt.xlabel('Name')
plt.show()