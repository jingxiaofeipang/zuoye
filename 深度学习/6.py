#step1:读入数据
import numpy as np
x_1 = np.array([0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,]).reshape([6,6])
t1 = 1
t2 = 0
t3 = 0
x_1   # 输入数据
x_1[0:3,1:4]
alpha = 0.2
w_F1 = np.array([-1.277,-0.454,0.358,1.138,-2.398,-1.664,-0.794,0.899,0.675]).reshape([3,3])
w_F2 = np.array([-1.274,2.338,2.301,0.649,-0.339,-2.054,-1.022,-1.204,-1.900]).reshape([3,3])
w_F3 = np.array([-1.869,2.044,-1.290,-1.710,-2.091,-2.946,0.201,-1.323,0.207]).reshape([3,3])
b_F1 = -3.363
b_F2 = -3.176
b_F3 = -1.739
print("w_F1:")
print(w_F1)
print("w_F2:")
print(w_F2)
print("w_F3:")
print(w_F3)
print("b_F1:")
print(b_F1)
print("b_F2:")
print(b_F2)
print("b_F3:")
print(b_F3)
w_O1_P1 = np.array([-0.276,0.124,-0.961,0.718]).reshape([2,2])
w_O1_P2 = np.array([-3.680,-0.594,0.280,-0.782]).reshape([2,2])
w_O1_P3 = np.array([-1.475,-2.010,-1.085,-0.188]).reshape([2,2])
w_O2_P1 = np.array([0.010,0.661,-1.591,2.189]).reshape([2,2])
w_O2_P2 = np.array([1.728,0.003,-0.250,1.898]).reshape([2,2])
w_O2_P3 = np.array([0.238,1.589,2.246,-0.093]).reshape([2,2])
w_O3_P1 = np.array([-1.322,-0.218,3.527,0.061]).reshape([2,2])
w_O3_P2 = np.array([0.613,0.218,-2.130,-1.678]).reshape([2,2])
w_O3_P3 = np.array([1.236,-0.486,-0.144,-1.235]).reshape([2,2])
b_O1 = 2.060
b_O2 = -2.746
b_O3 = -1.818
w_O1_P3[0:1,0:1]
'''计算'''
z_F1 = np.array([(x_1[0:3,0:3]*w_F1).sum(),(x_1[0:3,1:4]*w_F1).sum(),(x_1[0:3,2:5]*w_F1).sum(),(x_1[0:3,3:6]*w_F1).sum(),
                (x_1[1:4,0:3]*w_F1).sum(),(x_1[1:4,1:4]*w_F1).sum(),(x_1[1:4,2:5]*w_F1).sum(),(x_1[1:4,3:6]*w_F1).sum(),
                (x_1[2:5,0:3]*w_F1).sum(),(x_1[2:5,1:4]*w_F1).sum(),(x_1[2:5,2:5]*w_F1).sum(),(x_1[2:5,3:6]*w_F1).sum(),
                (x_1[3:6,0:3]*w_F1).sum(),(x_1[3:6,1:4]*w_F1).sum(),(x_1[3:6,2:5]*w_F1).sum(),(x_1[3:6,3:6]*w_F1).sum()]).reshape(4,4) + b_F1 
z_F1
(x_1[0:3,1:4] * w_F1).sum() + b_F1
z_F1[0:1,0:1]
z_F2 = np.array([(x_1[0:3,0:3]*w_F2).sum(),(x_1[0:3,1:4]*w_F2).sum(),(x_1[0:3,2:5]*w_F2).sum(),(x_1[0:3,3:6]*w_F2).sum(),
                (x_1[1:4,0:3]*w_F2).sum(),(x_1[1:4,1:4]*w_F2).sum(),(x_1[1:4,2:5]*w_F2).sum(),(x_1[1:4,3:6]*w_F2).sum(),
                (x_1[2:5,0:3]*w_F2).sum(),(x_1[2:5,1:4]*w_F2).sum(),(x_1[2:5,2:5]*w_F2).sum(),(x_1[2:5,3:6]*w_F2).sum(),
                (x_1[3:6,0:3]*w_F2).sum(),(x_1[3:6,1:4]*w_F2).sum(),(x_1[3:6,2:5]*w_F2).sum(),(x_1[3:6,3:6]*w_F2).sum()]).reshape(4,4) + b_F2 
z_F2
z_F3 = np.array([(x_1[0:3,0:3]*w_F3).sum(),(x_1[0:3,1:4]*w_F3).sum(),(x_1[0:3,2:5]*w_F3).sum(),(x_1[0:3,3:6]*w_F3).sum(),
                (x_1[1:4,0:3]*w_F3).sum(),(x_1[1:4,1:4]*w_F3).sum(),(x_1[1:4,2:5]*w_F3).sum(),(x_1[1:4,3:6]*w_F3).sum(),
                (x_1[2:5,0:3]*w_F3).sum(),(x_1[2:5,1:4]*w_F3).sum(),(x_1[2:5,2:5]*w_F3).sum(),(x_1[2:5,3:6]*w_F3).sum(),
                (x_1[3:6,0:3]*w_F3).sum(),(x_1[3:6,1:4]*w_F3).sum(),(x_1[3:6,2:5]*w_F3).sum(),(x_1[3:6,3:6]*w_F3).sum()]).reshape(4,4) + b_F3 
z_F3
z_F3[0:1,1:2]
# 定义sigmoid函数
def sigmoid(x):
    return 1/(1+np.exp(-x))
a_F1 = sigmoid(z_F1)
a_F1
a_F2 = sigmoid(z_F2)
a_F2
a_F3 = sigmoid(z_F3)
a_F3
a_F1[0:2,0:2].max()
P1 = np.array([a_F1[0:2,0:2].max(),a_F1[0:2,2:].max(),
              a_F1[2:,0:2].max(),a_F1[2:,2:].max()]).reshape([2,2])
P1
P2 = np.array([a_F2[0:2,0:2].max(),a_F2[0:2,2:].max(),
              a_F2[2:,0:2].max(),a_F2[2:,2:].max()]).reshape([2,2])
P2
P3 = np.array([a_F3[0:2,0:2].max(),a_F3[0:2,2:].max(),
              a_F3[2:,0:2].max(),a_F3[2:,2:].max()]).reshape([2,2])
P3
z_O1 = (P1 * w_O1_P1).sum() + (P2 * w_O1_P2).sum() + (P3 * w_O1_P3).sum() + b_O1
z_O1
z_O2 = (P1 * w_O2_P1).sum() + (P2 * w_O2_P2).sum() + (P3 * w_O2_P3).sum() + b_O2
z_O2
z_O3 = (P1 * w_O3_P1).sum() + (P2 * w_O3_P2).sum() + (P3 * w_O3_P3).sum() + b_O3
z_O3
a_O1 = sigmoid(z_O1)
a_O1
a_O2 = sigmoid(z_O2)
a_O2
a_O3 = sigmoid(z_O3)
a_O3
C = 1/2 * ( (t1 - a_O1)**2 + (t2 - a_O2)**2 + (t3 - a_O3)**2 )
print(C)
'''step4: 计算delta'''
# delta_O
delta_O_1 = (a_O1 - t1) * (sigmoid(z_O1))*(1-sigmoid(z_O1))
delta_O_2 = (a_O2 - t2) * (sigmoid(z_O2))*(1-sigmoid(z_O2))
delta_O_3 = (a_O3 - t3) * (sigmoid(z_O3))*(1-sigmoid(z_O3))
print("delta_O_1:",delta_O_1)
print("delta_O_2:",delta_O_2)
print("delta_O_3:",delta_O_3)
delta_F1_11 = (delta_O_1*w_O1_P1[0:1,0:1] + delta_O_2*w_O2_P1[0:1,0:1] + delta_O_3*w_O3_P1[0:1,0:1]) * 1 * (sigmoid(z_F1[0:1,0:1]))*(1-sigmoid(z_F1[0:1,0:1]))
delta_F1_11
delta_F3_11 = (delta_O_1*w_O1_P3[0:1,0:1] + delta_O_2*w_O2_P3[0:1,0:1] + delta_O_3*w_O3_P3[0:1,0:1]) * 1 * (sigmoid(z_F3[0:1,0:1]))*(1-sigmoid(z_F3[0:1,0:1]))
delta_F3_11
















