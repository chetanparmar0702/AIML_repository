from statistics import correlation
from zipfile import sizeEndCentDir

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# data_zero = {
#     'temperature': [25, 28, 30, 32, 35],
#     'ice_cream_sales': [150, 120, 100, 80, 60]
# }
# df_zero = pd.DataFrame(data_zero)
#
#
# corr_matrix_zero = df_zero.corr()
#
#
# plt.figure(figsize=(6, 4))
# sns.heatmap(corr_matrix_zero, annot=True, cmap='viridis', fmt=".2f")
# plt.title('Heatmap of Zero Correlation')
# plt.show()
#
# print(corr_matrix_zero)

# The number of passengers in a car does not have a linear relationship with the car('s average speed on a highway. '
# 'Create a Python script with a dataset to demonstrate this. Plot a heatmap to show the zero correlation.)

data_zero = {
    'number_passanger': [7, 5, 4, 3, 2],
    'car_speed': [105, 100, 90, 95, 110]
}
df_zero = pd.DataFrame(data_zero)


corr_matrix_zero = df_zero.corr()


plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix_zero, annot=True, cmap='viridis', fmt=".2f")
plt.title('Heatmap of Zero Correlation')
plt.show()

print(corr_matrix_zero)