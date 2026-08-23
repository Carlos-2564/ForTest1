import numpy as np


# a2 =np.array([[[1,2,3],[4,5,6]],
#                [[7,8,9],[10,11,12]]])
# print(a2)
# a=np.ones(3)
# print(a)
# a3=np.arange(3)
# print(a3)
# a4=np.eye()
# print(a4)
# data = np.array([[1, 2], [3, 4], [5, 6]])
# print(data[0, 1])    # 第0行第1列 → 2[reference:25]
# print(data[1:2])     # 切片获取第1到2行[reference:26]
# print(data[0:2, 0])  # 前两行第0列[reference:27]
# print(data.std())
# print(data.mean(axis=0))
data1 = np.array([1,2,3])
data2 = np.array([[1,10],[100,1000],[10000,100000]])
data3 = np.array([1,2,34])
print(data1.dot(data2))
print(np.cross(data1 ,data3))
print(np.outer(data1 ,data2))