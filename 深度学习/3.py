import numpy as np
x_1 = np.array([1,1,1,1,0,1,1,0,1,1,1,1]).reshape([12,1]) #书写矩阵，将矩阵改为12行1列的
x_1   # 输入数据
'''w_2'''
# 设置权重和隐藏层的初始值
np.random.seed(100)                 #随机数种子，确保每次生成的随机数都是一样的
# w_2_1n = np.random.randn(4,3).reshape([1,12])    # 生成标准正态分布的随机数
# b_2_1 = np.random.randn(1)

# w_2_2n = np.random.randn(4,3)     
# b_2_2 = np.random.randn(1)

# w_2_3n = np.random.randn(4,3)       
# b_2_3 = np.random.randn(1)
w_2 = np.random.randn(36).reshape(3,12)
print(w_2)
b_2 = np.random.randn(3).reshape(3,1)
print(b_2)
'''z_2'''
# 原数据与w点乘加b
z_2 = np.dot(w_2,x_1) + b_2 
z_2
'''a_2'''
a_2 = 1/(1+np.exp(-z_2))
a_2
'''w_3'''
np.random.seed(10)    #随机数种子，确保每次生成的随机数都是一样的
w_3 = np.random.randn(6).reshape(2,3) #根据给定的维数生成[)之间的数字，括号中一个参数是一维
print(w_3)
b_3 = np.random.randn(2).reshape(2,1)
print(b_3)
'''z_3'''
z_3 = np.dot(w_3,a_2) + b_3 
z_3
'''a_3'''
a_3 = 1/(1+np.exp(-z_3))
a_3
'''计算平方误差C'''
a_3[0]
C = 1/2 * ((1-a_3[0])**2 + (0-a_3[1])**2 )
C


