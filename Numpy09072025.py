# import numpy as np
#
# arr = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(arr)
#
#
# import numpy as np
# arr = np.arange(10)
# print(arr)
#
#
# import numpy as np
# arr = np.arange(2,10)
# print(arr)


# import numpy as np
# arr = np.arange(12)
# print(arr)
# reshaped_arr=np.reshape(arr,(3,4))
# print(reshaped_arr)

# import numpy as np
# arr = np.array([[1,2,3],
#                [4,5,6]])
# transposed_arr=np.transpose(arr)
# print(transposed_arr)

# import numpy as np
# arr = np.array([[1,2,3],
#                [4,5,6]])
# row_mean=np.mean(arr,axis=0)
# print(row_mean)
#
# import numpy as np
# arr = np.array([[1,2,3],
#                [4,5,6]])
# col_sum=np.sum(arr,axis=1)
# print(col_sum)
#
# import numpy as np
# rand_arr=np.random.rand(5)
# print(rand_arr)
#
#
# import numpy as np
# randn_arr=np.random.randn(5)
# print(randn_arr)
#
#
# import numpy as np
# arr1=np.array([1,2,3])
# arr2=np.array([[[3],[2],[1]]])
# print(arr1*arr2)
#
# import numpy as np
# arr1=np.array([1,2,3])
# arr2=np.array([[[3],[2],[1]]])
# print(np.multiply(arr1,arr2))
# print(np.matmul(arr1,arr2))

# Create a 2*3 and 3*2 matrix, show both mathematical and matrix multiplication

import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[1,2],[3,4],[5,6]])
print(np.matmul(arr1,arr2))
