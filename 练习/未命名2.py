# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:34:55 2024

@author: 25051
"""

#求f(x)=e**x在[-1,1]的最佳三次最佳平方逼近多项式，要求用{p0,p1,p2,p3}作基函数

from scipy.integrate import quad
import math

#定义Legendre多项式
def p0(x):
    return 1
def p1(x):
    return x
def p2(x):
    return 1/2 * (3*x**2-1)
def p3(x):
    return 1/2 * (5*x**3-3*x)



#设置函数
def f(x):
    return math.e**x


#计算内积
def inner_product(func1, func2, a, b):
    integrand = lambda x: func1(x) * func2(x)
    result, error = quad(integrand, a, b)
    return result


#fenzi是p函数和f函数的内积，分母是p函数和p函数的内积
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


print(f"三次最佳三次最佳平方逼近多项式为{a0}+{a1}*x+{a2}*x**2+{a3}*x**3")


def approximating_polynomial(x):
     
    return str(a0*p0(x)+a1*p1(x)+a2*p2(x)+a3*p3(x))
 
number = int(input("输入要计算的三次最佳平方逼近多项式的x:"))

jie = approximating_polynomial(number)
print(jie)
















