import numpy as np
import torch
x_1 = torch.tensor([1,1,1,1,0,1,1,0,1,1,1,1]).reshape(12,1)  #12行1列
x_1   # 输入数据
# 框架
# 第一个隐藏层有3个神经单元
n_hidden = 3
# 输入的样本有12个特征
n_input = 12
# 手写数字分为0 1 这2个类别
n_classes = 2
import torch
# 设置权重和隐藏层的初始值                   
torch.manual_seed(100) #随机数种子设置为 100，以确保后续的随机操作在相同的环境下产生相同的结果
w_2_1n = torch.randn(4,3).reshape(1,12)       # 生成标准正态分布的随机数
b_2_1 = torch.randn(1) #创建了一个形状为1的张量,其中的元素是从均值为0标准差为1的正态分布中随机采样得到的。

w_2_2n = torch.randn(4,3)      
b_2_2 = torch.randn(1)

w_2_3n = torch.randn(4,3)       
b_2_3 = torch.randn(1)
w_2_1n
b_2_1
print(w_2_1n,b_2_1)
print(w_2_2n,b_2_2)
print(w_2_3n,b_2_3)
# 原数据与w点乘加b
z_2_1 = torch.dot(w_2_1n,x_1)
a_2 = 1/(1+np.exp(-z_2_1))
a_3 = 1/(1+np.exp(-z_3_1))
x_1 = torch.tensor([1,1,1,1,0,1,1,0,1,1,1,1])
x_1.shape 
w_2_1n.shape 
np.dot(w_2_1n,x_1)
w_2_1n
t = torch.zeros(4,3)
t
z_2_1 = torch.addcmul(t,-2.3652,x_1,w_2_1n) 
#torch.addcmul?
a_2_1 = torch.sigmoid(z_2_1)
C = 1/2 * ((1-a_3_1)**2 + (0-a_3_2)**2)