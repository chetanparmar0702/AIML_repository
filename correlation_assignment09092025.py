# The Law of Demand states that as the price of a good increases, the quantity demanded by consumers decreases. Create a Python script to model this relationship.
# Calculate the correlation and plot a heatmap to visualize the strong negative correlation.

# Negative correlation

from statistics import correlation
from zipfile import sizeEndCentDir

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# data = { 'Price_of_the_goods': [100, 200, 300, 400, 500], 'Quantity_demand': [10, 9, 8, 7, 6] }
# df_negative = pd.DataFrame(data)
#
#
# corr_matrix_negative = df_negative.corr()
#
#
# plt.figure(figsize=(6, 4))
# sns.heatmap(corr_matrix_negative, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Negative Correlation')
# plt.show()


# The Law of Supply states that as the price of a good increases, the quantity supplied by producers also increases. Create a Python script to model this relationship using a dataset.
# Calculate the correlation coefficient and plot a heatmap to visualize the  correlation.

data = { 'Price_of_the_goods': [100, 200, 300, 400, 500], 'Quantity_demand': [20, 40, 60, 80, 100] }

df_positive = pd.DataFrame(data)


corr_matrix_positive = df_positive.corr()


plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix_positive, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Positive Correlation')
plt.show()