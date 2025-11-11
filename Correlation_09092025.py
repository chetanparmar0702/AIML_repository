from statistics import correlation
from zipfile import sizeEndCentDir

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



# data = {
#     'Study_Hours': [1, 2, 3, 4, 5],
#     'Test_Score': [60, 70, 80, 90, 95]
# }
# df_positive = pd.DataFrame(data)
#
#
# corr_matrix_positive = df_positive.corr()
#
#
# plt.figure(figsize=(6, 4))
# sns.heatmap(corr_matrix_positive, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Heatmap of Positive Correlation')
# plt.show()

# Negative correlation

# data = { 'Hours_of_Exercise_Per_Week': [1, 2, 3, 4, 5], 'Body_Weight_kg': [85, 80, 75, 70, 65] }
# df_negative = pd.DataFrame(data)
#
#
# corr_matrix_negative = df_negative.corr()
#
#
# plt.figure(figsize=(6, 4))
# sns.heatmap(corr_matrix_negative, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Excercise Negative Correlation')
# plt.show()


# trunk_size
data_zero = {
    'Tank_Size_Litres': [40, 45, 50, 55, 60],
    'Fuel_Efficiency_KMPL': [15, 12, 18, 11, 14]
}
df_zero = pd.DataFrame(data_zero)


corr_matrix_zero = df_zero.corr()


plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix_zero, annot=True, cmap='viridis', fmt=".2f")
plt.title('Heatmap of Zero Correlation')
plt.show()

print(corr_matrix_zero)