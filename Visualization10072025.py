import matplotlib.pyplot as plt
import numpy as np

#line plot
# x=[1,2,3,4,5]
# y=[2,3,5,7,11]
#
# plt.plot(x,y)
# plt.xlabel('X-axis Label')
# plt.ylabel('Y-axis Label')
# plt.title('Line Plot')
# plt.show()

#Scatter plot
# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[2,3,5,7,11]
#
# plt.scatter(x,y)
# plt.xlabel('X-axis Label')
# plt.ylabel('Y-axis Label')
# plt.title('Scatter Plot')
# plt.show()

#Bar plot
# x=['A','B','C','D','E']
# y=[10,15,7,10,12]
#
# plt.bar(x,y)
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Bar Plot')
# plt.show()
#
# #Histogram
# import numpy as np
# data=np.random.randn(1000)
# plt.hist(data,bins=3)
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histogram')
# plt.show()
#
# #piechart
#
# sizes=[15,30,45,10]
# labels=['A','B','C','D']
# plt.pie(sizes,labels=labels,autopct='%1.1f%%')
# plt.title('Pie Chart')
# plt.show()


sales_data = [-1000, -100,-10, 10, 20,30, 100, 150, 120, 180, 200, 210, 220,
              230, 240, 250, 260, 270, 280, 290, 300,500, 800, 1000]
plt.figure(figsize=(8,5))
plt.boxplot(sales_data)
plt.title('Sales Data')
plt.xlabel('Sales')
plt.show()
# q1=np.percentile(sales_data, 25)
# print(q1)
# q3=np.percentile(sales_data, 75)
# print(q3)
# iqr= q3-q1
#
# lower_bound = q1 - 1.5 * iqr
# print(lower_bound)
# upper_bound = q3 + 1.5 * iqr
# print(upper_bound)
# outliers= [i for i in sales_data if i<lower_bound or i> upper_bound]
# print(outliers)
