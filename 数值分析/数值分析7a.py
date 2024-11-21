# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:47:53 2024

@author: 25051
"""

def bisect(f, a, b, tol=1e-6, max_iter=100):
    
    
    
    if f(a) * f(b) >= 0:
        print("函数在区间两端的值符号相同，请检查输入。")
        return None
    
    
    
    
    
    
    for i in range(max_iter):
        c = (a + b) / 2  # 计算区间中点
        if f(c) == 0 or (b - a) / 2.0 < tol:  # 检查是否满足容忍误差或达到最大迭代次数
            return c
        if f(a) * f(c) < 0:  # 根在区间[a, c]内
            b = c
        else:  # 根在区间[c, b]内
            a = c
    return (a + b) / 2  # 返回最终的近似根


def func(x):
    return x**3-x-1

# 调用二分法函数
root = bisect(func, 1.0, 1.5)  # 假设根在区间[0, 2]内
print(f"由二分法得到方程 x^3 - x-1= 0 的根是：{root:.2f}")














