import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
data= [-200, 155,160,162,165,168,170,172,175,178,180,182,185,195,205,163,600]
mean = np.mean(data)
print(mean)
median = np.median(data)
print(median)
mode = stats.mode(data, keepdims=True).mode[0]
print(mode)
std_dev = np.std(data, ddof=0)
print(std_dev)
variance= np.var(data)
print(variance)


q1=np.percentile(data, 25)
print(q1)
q3=np.percentile(data, 75)
print(q3)
iqr= q3-q1
print(iqr)

lower_bound = q1 - 1.5 * iqr
print(lower_bound)
upper_bound = q3 + 1.5 * iqr
print(upper_bound)
outliers= [i for i in data if i<lower_bound or i> upper_bound]
print(outliers)

plt.figure(figsize=(8,5))
plt.boxplot(data)
plt.title('Sales Data')
plt.xlabel('Sales')
plt.show()
