# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:34:55 2024

@author: 25051
"""

#求f(x)=e**x在[-1,1]的最佳三次最佳平方逼近多项式，要求用{p0,p1,p2,p3}作基函数

from scipy.integrate import quad
import math
import numpy as np


#定义Legendre多项式
def p0():
    return np.poly1d([1])  # 表示多项式 x^2 + 2x + 3
def p1():
    return np.poly1d([1,0])
def p2():
    return np.poly1d([3/2,0,-1/2])
def p3():
    return np.poly1d(5/2,0,-3/2,0)



#设置函数
def f(x):
    return math.e**x


#计算内积
def inner_product(func1, func2, a, b):
    integrand = lambda x: func1(x) * func2(x)
    result, error = quad(integrand, a, b)
    return result


fenzi0 = inner_product(f, p0, -1, 1)
fenmu0 = inner_product(p0, p0, -1, 1)
fenzi1 = inner_product(f, p1, -1, 1)
fenmu1 = inner_product(p1, p1, -1, 1)
fenzi2 = inner_product(f, p2, -1, 1)
fenmu2 = inner_product(p2, p2, -1, 1)
fenzi3 = inner_product(f, p3, -1, 1)
fenmu3 = inner_product(p3, p3, -1, 1)


#计算系数
a0 = fenzi0 / fenmu0
a1 = fenzi1 / fenmu1
a2 = fenzi2 / fenmu2
a3 = fenzi3 / fenmu3



#构建多项式
def approximating_polynomial(x):
     
    return a0*p0(x)+a1*p1(x)+a2*p2(x)+a3*p3(x)
    
poly0 = p0()
poly1 = p1()
poly2 = p2()
poly3 = p3()

print(poly0)

















