# -*- coding: utf-8 -*-

#



import numpy as np

# 定义目标函数
def f(x, y):
    return x**2 + y**2

# 计算梯度
def gradient(x, y):
    return np.array([2*x, 2*y])

# 梯度下降法
def gradient_descent(starting_point, learning_rate, cishu):
    x, y = starting_point
    for i in range(cishu):
        grad = gradient(x, y)
        x -= learning_rate * grad[0]
        y -= learning_rate * grad[1]
        if i % 1 == 0:  # 
            print(f"计算第 {i}次: x = {x:.2f}, y = {y:.2f}, z = {f(x, y):.2f}")
    return x, y

# 初始点，学习率和迭代次数
starting_point = (3, 2)
learning_rate = 0.1
cishu = 50

# 执行
x_min, y_min = gradient_descent(starting_point, learning_rate, cishu)
print(f"50次梯度下降后: x = {x_min:.2f}, y = {y_min:.2f}, z = {f(x_min, y_min):.2f}")