import numpy as np
from scipy import stats
from collections import Counter
data= [30,18,25,30,30,18]

mean = np.mean(data)
print(mean)
median = np.median(data)
print(median)
mode = stats.mode(data, keepdims=True).mode[0]
print(mode)
count= Counter(data)
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

# N= [10, 30, 1, 20]
# max=10
# for i in N:
#     if  i>max:
#         max=i
# print(max)
# min=20
# for i in N:
#     if  i<min:
#         min=i
# print(min)