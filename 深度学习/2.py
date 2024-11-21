# 定义函数
def func_1(x, y):
    return x**2 + y**2

# 初始化，定义学习率
def gradient_descent():
    x = 3.0
    y = 2.0
    z = func_1(x, y)
    eta = 0.1  # 学习率
    for i in range(30):
        print(i)
        print("第{}次迭代:  x={:.2f},  y={:.2f},  z={:.2f}".format((i+1), x, y, z))
        x -= eta * 2 * x  # 更新 x
        y -= eta * 2 * y  # 更新 y
        z = func_1(x, y)  # 重新计算 z

# 调用梯度下降函数
gradient_descent()

# 打印0-30序列
for i in range(31):
    print(i)
