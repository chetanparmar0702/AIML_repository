import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    'Region': ['North', 'South', 'East', 'West'] * 5,
    'Sales': [2300, 1800, 2500, 2200, 2400, 2100, 2600, 2300, 2000, 1900,
              2700, 2250, 2600, 2150, 2800, 2100, 2200, 2050, 2300, 2400],
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'] * 4
}

df = pd.DataFrame(data)
# df = pd.read_csv('filename')
# print(df.head())
# Bar Plot: Average Sales by Region
plt.figure(figsize=(8, 5))
sns.barplot(x='Region', y='Sales', data=df)
plt.title('Bar Plot: Average Sales by Region')
plt.ylabel('Average Sales')
plt.xlabel('Region')
plt.show()

# Line Plot: Sales Trend per Region by Month
plt.figure(figsize=(8, 5))
sns.lineplot(x='Month', y='Sales', hue='Region', data=df, marker="o")
plt.title('Line Plot: Monthly Sales Trend by Region')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.show()

# Scatter Plot: Advertisement Spend vs Sales
df['Ad_Spend'] = [300, 250, 320, 310, 340, 290, 330, 280, 270, 300,
                  350, 310, 360, 300, 370, 310, 300, 290, 330, 320]

plt.figure(figsize=(8, 5))
sns.scatterplot(x='Ad_Spend', y='Sales', hue = 'Region', data=df)
plt.title('Scatter Plot: Advertisement Spend vs Sales')
plt.xlabel('Ad Spend')
plt.ylabel('Sales')
plt.show()

# Histogram of Sales
plt.figure(figsize=(8, 5))
sns.histplot(df['Sales'], kde=False, bins=10, color='skyblue')
plt.title('Histogram: Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# KDE Plot of Sales
plt.figure(figsize=(8, 5))
sns.kdeplot(df['Sales'], fill=True, color='green')
plt.title('KDE Plot: Sales Density')
plt.xlabel('Sales')
plt.ylabel('Density')
plt.show()

# Box Plot: Sales by Region
plt.figure(figsize=(8, 5))
sns.boxplot(x='Region', y='Sales', data=df)
plt.title('Box Plot: Sales Distribution by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()

#P=25/100×(n−1)+1
#P = 75/100*(n-1)+1