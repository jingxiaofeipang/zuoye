# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:01:29 2024

@author: 25051
"""

import math
from typing import final

xn = [(math.pi/6,1/2),(math.pi/4,1/(2**(1/2))),(math.pi/3,(3**(1/2)/2))]
x = float(input("输入要计算的lagrance插值x:"))*(math.pi/180)

#当n=1时
def lagranceone(flag):
    if flag == 1:
        lagrange = (x-xn[1][0])/(xn[0][0]-xn[1][0])*xn[0][1]+(x-xn[0][0])/(xn[1][0]-xn[0][0])*xn[1][1]

    if flag == 2:
        lagrange = (x - xn[2][0]) / (xn[1][0] - xn[2][0]) * (xn[1][1]) + (x - xn[1][0]) / (xn[2][0] - xn[1][0]) * (xn[2][1])


    return lagrange

def lagrancetwo():
    lagrange = ((x - xn[1][0]) * (x - xn[2][0])) / ((xn[0][0] - xn[1][0]) * (xn[0][0] - xn[2][0])) * xn[0][1] + (
                (x - xn[0][0]) * (x - xn[2][0])) / ((xn[1][0] - xn[0][0]) * (xn[1][0] - xn[2][0])) * xn[1][1] + (
                           (x - xn[0][0]) * (x - xn[1][0])) / ((xn[2][0] - xn[0][0]) * (xn[2][0] - xn[1][0])) * xn[2][1]
    return lagrange



print(f"利用x0，x1计算的sin{x}值为{lagranceone(1)}")
print(f"利用x1，x2计算的sin{x}值为{lagranceone(2)}")
print(f"2次计算的lagrance值为{lagrancetwo()}")

def erro(flag):
    if flag == 1:   #计算当n=1时的余项误差
        erroyou = (1/2)*(x-xn[0][0])*(x-xn[1][0])*(-1/2)
        errozuo = (1/2)*(x-xn[0][0])*(x-xn[1][0])*(-((3**(1/2))/2))
        finalerro = math.sin(x)-lagranceone(1)
        if finalerro>errozuo and finalerro<erroyou:
            print(f"x0和x1推出的sin{x}误差在范围之内,误差为{finalerro}")
        else:
            print(f"x0和x1推出的sin{x}误差在不在范围之内")

    elif flag == 2:
        """
          当 flag=2 时，计算lagrange_one(2) 所产生的误差。
        """
        erroZuo = ((x) - (xn[1][0])) * ((x - (xn[2][0])) / 2) * (-1 / (2 ** (1 / 2)))
        erroYou = ((x) - (xn[1][0])) * ((x - (xn[2][0])) / 2) * (-((3 ** (1 / 2)) / 2))
        erroFinal = math.sin(x) - lagranceone(2)
        if erroFinal > erroZuo and erroFinal < erroYou:
            print(f"利用x1,x2推导出sin{x}°的值的误差在可接受范围内，且误差为:{erroFinal}")
        else:
            print(f"利用x1,x2推导出sin{x}°的值的误差过大，请重新设计。（误差为：{erroFinal}）")
    elif flag == 3:
        """
          当 flag=3 时，计算lagrange_two() 所产生的误差。
        """
        erroYou = ((x) - (xn[0][0])) * (((x) - (xn[1][0]))) * ((x) - (xn[2][0])) * (-(3 ** (1 / 2)) / 2) / (3 * 2 * 1)
        erroZuo = ((x) - (xn[0][0])) * (((x) - (xn[1][0]))) * ((x) - (xn[2][0])) * (-1 / 2) / (3 * 2 * 1)
        erroFinal = math.sin(x) - lagrancetwo()
        if erroFinal > erroZuo and erroFinal < erroYou:
            print(f"利用sinx的2次lagrange插值计算可推导出sin{x}°的值的误差在可接受范围内，且误差为:{erroFinal}")
        else:
            print(f"利用sinx的2次lagrange插值计算可推导出sin{x}°的值的误差过大，请重新设计。（误差为：{erroFinal}）")

erro(1)
erro(2)
erro(3)