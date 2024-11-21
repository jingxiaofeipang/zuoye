import math

# 已知的正弦值
xn = [(math.pi/6, 1/2), (math.pi/4, 1/(2**(1/2))), (math.pi/3, (3**(1/2)/2))]

# 输入转换为弧度
x = float(input("请输入需要估算的sin函数的自变量x（角度）:")) * (math.pi / 180)

# 1次拉格朗日插值
def lagrange_one(flag, x, xn):
    if flag == 1:
        return (x-xn[1][0])/(xn[0][0]-xn[1][0])*(xn[0][1]) + (x-xn[0][0])/(xn[1][0]-xn[0][0])*(xn[1][1])
    elif flag == 2:
        return (x-xn[2][0])/(xn[1][0]-xn[2][0])*(xn[1][1]) + (x-xn[1][0])/(xn[2][0]-xn[1][0])*(xn[2][1])
    else:
        return 0

# 2次拉格朗日插值
def lagrange_two(x, xn):
    result = 0
    for i in range(len(xn)):
        term = xn[i][1]
        for j in range(len(xn)):
            if i != j:
                term *= (x - xn[j][0]) / (xn[i][0] - xn[j][0])
        result += term
    return result

# 计算1次和2次拉格朗日插值
result1_1 = lagrange_one(1, x, xn)
result1_2 = lagrange_one(2, x, xn)
result2 = lagrange_two(x, xn)

# 计算实际的正弦值
actual_value = math.sin(x)

# 打印结果
print(f'利用x0,x1可推导出sin({x*180/math.pi:.2f}°)的值为: {result1_1:.4f}')
print(f'利用x1,x2可推导出sin({x*180/math.pi:.2f}°)的值为: {result1_2:.4f}')
print(f'利用sinx的2次Lagrange插值计算可推导出sin({x*180/math.pi:.2f}°)的值为: {result2:.4f}')
print(f'实际的sin({x*180/math.pi:.2f}°)的值为: {actual_value:.4f}')

# 计算误差
def erro(flag, x, xn, actual_value):
    if flag == 1:
        result = lagrange_one(1, x, xn)
        erroZuo = ((x)-(xn[0][0]))*((x-(xn[1][0]))/2)*(-((3**(1/2))/2))
        erroYou = ((x)-(xn[0][0]))*((x-(xn[1][0]))/2)*(-1/2)
    elif flag == 2:
        result = lagrange_one(2, x, xn)
        erroZuo = ((x)-(xn[1][0]))*((x-(xn[2][0]))/2)*(-1/(2**(1/2)))
        erroYou = ((x)-(xn[1][0]))*((x-(xn[2][0]))/2)*(-((3**(1/2))/2))
    elif flag == 3:
        result = lagrange_two(x, xn)
        erroZuo = ((x)-(xn[0][0]))*(((x)-(xn[1][0])))*((x)-(xn[2][0]))*(-1/2)/(3*2*1)
        erroYou = ((x)-(xn[0][0]))*(((x)-(xn[1][0])))*((x)-(xn[2][0]))*(-(3**(1/2))/2)/(3*2*1)

    erroFinal = abs(actual_value - result)
    if erroZuo < erroFinal < erroYou:
        print(f"误差在可接受范围内，且误差为:{erroFinal:.4f}")
    else:
        print(f"误差过大，请重新设计。（误差为：{erroFinal:.4f}）")

erro(1, x, xn, actual_value)
erro(2, x, xn, actual_value)
erro(3, x, xn, actual_value)

