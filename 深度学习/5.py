# 读入手写数字的 图像 和 正解 
import numpy as np
x_1 = np.array([1,1,1,1,0,1,1,0,1,1,1,1]).reshape([12,1])   # 手写数字为0
print(x_1)  
t1 = 1
t2 = 0
np.random.seed(100) 

w_2 = np.random.randn(36).reshape(3,12)
print(w_2)
b_2 = np.random.randn(3).reshape(3,1)
print(b_2)
print()

w_3 = np.random.randn(6).reshape(2,3)
print(w_3)
b_3 = np.random.randn(2).reshape(2,1)
print(b_3)

alpha = 0.2    # 设置学习率（学习率的设置需要反复试错）
w_3[0,1]
z_2 = np.dot(w_2,x_1) + b_2
print("z_2如下")
print(z_2)
a_2 = 1/(1+np.exp(-z_2))
print("a_2如下")
print(a_2)
z_3 = np.dot(w_3,a_2) + b_3
print("z_3如下")
print(z_3)
a_3 = 1/(1+np.exp(-z_3))
print("a_3如下")
print(a_3)
C = 1/2 * ( (t1-a_3[0])**2 + (t2-a_3[1])**2 )
print(C)
'''step4：计算各层神经单元误差（delta）'''
# 定义sigmoid函数
def sigmoid(x):
    return 1/(1+np.exp(-x))
delta_3_1 = (a_3[0]-t1)*(sigmoid(z_3[0]))*(1-sigmoid(z_3[0]))
print(delta_3_1)
delta_3_2 = (a_3[1]-t2)*(sigmoid(z_3[1]))*(1-sigmoid(z_3[1]))
print(delta_3_2)
delta_2_1 = ((delta_3_1*w_3[0,0]) + (delta_3_2*w_3[1,0])) * sigmoid(z_2[0]) * (1-sigmoid(z_2[0]))
print(delta_2_1)
delta_2_2 = ((delta_3_1*w_3[0,1]) + (delta_3_2*w_3[1,1])) * sigmoid(z_2[1]) * (1-sigmoid(z_2[1]))
print(delta_2_2)
delta_2_3 = ((delta_3_1*w_3[0,2]) + (delta_3_2*w_3[1,2])) * sigmoid(z_2[2]) * (1-sigmoid(z_2[2]))
print(delta_2_3)
'''step5:根据神经单元误差（delta）计算平方误差C的偏导数'''
# 对b求偏导 -> 表示好像不准确
b_3_1 = delta_3_1
b_3_2 = delta_3_2
b_2_1 = delta_2_1
b_2_2 = delta_2_2
b_2_3 = delta_2_3
# 对w求偏导
w_3_11 = delta_3_1 * a_2[0]
w_3_12 = delta_3_1 * a_2[1]
w_3_13 = delta_3_1 * a_2[2]
w_3_21 = delta_3_2 * a_2[0]
w_3_22 = delta_3_2 * a_2[1]
w_3_23 = delta_3_2 * a_2[2]
w_2_11 = delta_2_1 * x_1[0]
w_2_12 = delta_2_1 * x_1[1]
w_2_13 = delta_2_1 * x_1[2]
w_2_14 = delta_2_1 * x_1[3]
w_2_15 = delta_2_1 * x_1[4]
w_2_16 = delta_2_1 * x_1[5]
w_2_17 = delta_2_1 * x_1[6]
w_2_18 = delta_2_1 * x_1[7]
w_2_19 = delta_2_1 * x_1[8]
w_2_110 = delta_2_1 * x_1[9]
w_2_111 = delta_2_1 * x_1[10]
w_2_112 = delta_2_1 * x_1[11]
w_2_21 = delta_2_2 * x_1[0]
w_2_22 = delta_2_2 * x_1[1]
w_2_23 = delta_2_2 * x_1[2]
w_2_24 = delta_2_2 * x_1[3]
w_2_25 = delta_2_2 * x_1[4]
w_2_26 = delta_2_2 * x_1[5]
w_2_27 = delta_2_2 * x_1[6]
w_2_28 = delta_2_2 * x_1[7]
w_2_29 = delta_2_2 * x_1[8]
w_2_210 = delta_2_2 * x_1[9]
w_2_211 = delta_2_2 * x_1[10]
w_2_212 = delta_2_2 * x_1[11]
w_3_11 = delta_3_1 * x_1[0]
w_3_12 = delta_3_1 * x_1[1]
w_3_13 = delta_3_1 * x_1[2]
w_3_14 = delta_3_1 * x_1[3]
w_3_15 = delta_3_1 * x_1[4]
w_3_16 = delta_3_1 * x_1[5]
w_3_17 = delta_3_1 * x_1[6]
w_3_18 = delta_3_1 * x_1[7]
w_3_19 = delta_3_1 * x_1[8]
w_3_110 = delta_3_1 * x_1[9]
w_3_111 = delta_3_1 * x_1[10]
w_3_112 = delta_3_1 * x_1[11]
print(w_3_112)
