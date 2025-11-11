# Find mean median mode variance of the following dataset [10, 13, 12, 8, 23, 32]
from statistics import variance

import numpy as np
from collections import Counter

from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray
from scipy import stats

# data= [10,13,12,8,26,32]
# mean = np.mean(data)
# print(mean)
# median = np.median(data)
# print(median)
# mode = stats.mode(data, keepdims=True).mode[0]
# print(mode)
# std_dev = np.std(data, ddof=0)
# print(std_dev)
# print(std_dev**2)
# variance= np.var(data)
# print(variance)


# spending = [15, 25, 50, -10, 25, 100,-5]
# clean= [i for i in spending if i>0]
# print(clean)
# mean= np.mean(clean)
# print(mean)
# median= np.median(clean)
# print(median)
# mode= stats.mode(clean, keepdims=True).mode[0]
# print(mode)

# You have a dataset of house prices with some missing values.
# Prices = [350000, 420000, 280000, None, 480000, None].
# Separate the valid prices from None values, Median of the valid price, New list where None is replaced by median
# Prices = [350000, 420000, 280000, None, 480000, None]
# x= [i for i in Prices if i is not None]
# print(x)
# median= np.median(x)
# print(median)
# new_list=[i if i is not None else median for i in Prices]
# print(new_list)
#
# li=[1,2,3,4,5]
# li1 = [i * 10 for i in li]
# print(li1)

# Write a python program to check most frequent category.
purchases = ['electronics','apparel','home_goods','apparel','electronics','food','home_goods']
count= Counter(purchases)
print(count)
for i,j in count.items():
    print(i,j)
max=0
for i in count.values():
    if i> max:
        max=i
Number= []
for item, i in count.items():
    if i==max:
        Number.append(item)
print(Number)