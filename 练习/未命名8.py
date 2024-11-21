# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:46:56 2024

@author: 25051
"""
"""
import numpy as np
arr1 = np.array([1,2,3])
print(arr1)

arr2 = arr1.astype(float)
print(arr2)

arr3 = arr2.astype(int)
print(arr3)

#整数型数组与浮点数做运算，值不变，但会变成浮点数类型
print( arr1 + 1.0 )

#整数型数组遇到除法，即使除以整数
print(arr1 / 1)

#整数型数组和浮点型数组做运算
int_arr= np.array([1,2,3])
float_arr = np.array([1.0,2,3])
print(int_arr+float_arr)
"""
import numpy as np
"""
#一维数组
arr1 = np.ones(3)
print(arr1)

#二维数组
arr2 = np.ones((1,3))
print(arr2)

#三维数组
arr3 = np.ones((1,1,3))
print(arr3)




arr2 = np.arange(10).reshape(2, 5)
print(arr2)

print(arr2.reshape(2,-1))

#创建一维数组   向量
arr1 = np.array([1,2,3])
print(arr1)

#创建二维数组   行矩阵
arr2 = np.array([[1,2,3]])
print(arr2)

#创建二维数组   列矩阵
arr3 = np.array([[1],[2],[3]])
print(arr3)

import numpy as np
#创建二维数组  矩阵
arr4 = np.array([[1,2,3],[4,5,6]])
print(arr4)
arr5 = arr4.reshape(-1)
print(arr5)


arr1 = np.zeros(3)
print(arr1)
arr2 = np.zeros((1,3))
print(arr2)

arr3 = 3.14 * np.ones((2,3))
print(arr3)

#创建0-1均匀分布的浮点型随机数据
arr4 = np.random.random((3,3))
print(arr4)
arr5 = 40 * np.random.random((3,3))+60
print(arr5)

#整数型随机数组
arr1 = np.random.randint(10,100,(1,15))
print(arr1)

#服从正态分布的随机数组
arr3 = np.random.normal(0,1,(2,3))   #0:均值 1：标准差 （2，3）形状
print(arr3)



arr1 = np.arange(10 )
print(arr1)
arr2 = arr1
arr2[0]=100
print(arr2)
print(arr1)


arr1 = np.arange(1,4)
print(arr1)
arr2 = arr1.reshape(1,-1)
print(arr2)
arr3 = arr2.T
print(arr3)
"""


import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1)
arr2 = np.array([[7,8,9],[10,11,12]])
print(arr2)
#矩阵的拼接
arr3 = np.concatenate([arr1,arr2])
print(arr3)



