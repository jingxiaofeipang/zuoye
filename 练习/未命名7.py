# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:43:45 2024

@author: 25051
"""

import numpy as np
"""


arr = np.zeros([3, 3])
print(arr)


arr1 = np.empty((3,4))
print(arr1)

arr = np.zeros_like(arr1)
print(arr)

nd9 = np.random.random([5,5])
np.savetxt(fname='D:\121.txt', X=nd9)
nd10 = np.loadtxt('D:\121.txt')
print(nd10)

np.random.seed(2019)
nd11 = np.random.random(10)
print(nd11)
nd11[3]

print(nd11[3:6])

nd12 = np.arange(25).reshape(5, 5)
print(nd12)
print(nd12[1:3,1:3])

X = np.random.rand(2,3)
print(X)

def sigmoid(x):
    return 1/(1+np.exp(-X))
print("输入参数X的形状：",X.shape)
print("激活函数sigmoid输出形状：",sigmoid(X).shape)


arr2 = np.arange(24).reshape(2,3,4)
print(arr2)
print(arr2.transpose(1,2,0).shape)

"""


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print (np.stack((a,b),axis = 0))





