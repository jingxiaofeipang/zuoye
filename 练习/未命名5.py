# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:10:48 2024

@author: 25051
"""

import numpy as np
import matplotlib.pyplot as plt

# 定义函数f(x, y)
def f(x, y):
    return y - (2 * x) / y

# Euler显式方法
def euler_explicit(x0, y0, h, x_end):
    x = np.arange(x0, x_end + h, h)
    y = np.zeros(len(x))
    y[0] = y0
    for i in range(1, len(x)):
        y[i] = y[i-1] + h * f(x[i-1], y[i-1])
    return x, y

# 初始条件和参数
x0 = 0
y0 = 1
h = 0.01  # 步长
x_end = 1

# 执行Euler显式方法
x, y = euler_explicit(x0, y0, h, x_end)

# 绘制结果
plt.plot(x, y, label='Euler Explicit Method')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of Initial Value Problem using Euler Explicit Method')
plt.legend()
plt.show()