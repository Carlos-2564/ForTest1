# import numpy as np


# # a2 =np.array([[[1,2,3],[4,5,6]],
# #                [[7,8,9],[10,11,12]]])
# # print(a2)
# # a=np.ones(3)
# # print(a)
# # a3=np.arange(3)
# # print(a3)
# # a4=np.eye()
# # print(a4)
# # data = np.array([[1, 2], [3, 4], [5, 6]])
# # print(data[0, 1])    # 第0行第1列 → 2[reference:25]
# # print(data[1:2])     # 切片获取第1到2行[reference:26]
# # print(data[0:2, 0])  # 前两行第0列[reference:27]
# # print(data.std())
# # print(data.mean(axis=0))
# data1 = np.array([1,2,3])
# data2 = np.array([[1,10],[100,1000],[10000,100000]])
# data3 = np.array([1,2,34])
# print(data1.dot(data2))
# print(np.cross(data1 ,data3))
# print(np.outer(data1 ,data2))




# import numpy as np
# import torch
# # a2 =np.array([[[1,2,3],[4,5,6]],
# #                [[7,8,9],[10,11,12]]])
# # print(a2)
# # a=np.ones((3,4,2))
# # # print(a)
# # # a3=np.random.random((3,3))
# t2=torch.randn(4,3)
# # # print(a3)
# # # a4=torch.arange(4)
# # a5=torch.tensor([1,2,2,3])
# # a6=torch.dot(a4,a5)
# # print(a6)
# #
# t1=torch.arange(12,dtype=torch.float).reshape(3,4)
# #
# #
# # # print(t1)
# # # print(t1[ 0:2])
# # # print(t1[:, 0:2])
# #
# # print(t1)
# # print(t2)
# # t2=torch.randn(4,3)
# # t1=torch.arange(12,dtype=torch.float).reshape(3,4)
# # print(t1@t2)

#
# x = torch.tensor([[1, 5], [3, 2], [4, 6]])
#
# # 沿着行方向（dim=0，即跨行比较）求每列的最小值
# values, indices = torch.min(x, dim=0)
#
# print(x)
# print(values)   # tensor([1, 2])   -> 第0列最小是1，第1列最小是2
# print(indices)  # tensor([0, 1])   -> 第0列最小值在第0行，第1列最小值在第1行