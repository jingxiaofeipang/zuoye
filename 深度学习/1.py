# 求函数（fxy）的函数值
def fxy(x,y):
    return x**2+y**2
# 梯度下降法
def gradient_descent():
    times = 30  # 迭代次数
    alpha = 0.1   # 学习率定义为：0.1
    x = 3   # x的初始值
    y = 2   # y的初始值
    
    # 梯度下降算法
    for i in range(times):
        x = x - alpha * (2 * x)
        y = y - alpha * (2 * y)
        f = fxy(x,y)
        print("第%d次迭代：x=%f,y=%f,fxy=%f" % (i+1,x,y,f))
        
# gradient_descent()
if __name__ == "__main__":
    gradient_descent()


'''练习'''
#experience
def z_number(x,y):
    return x**2+y**2 
def gradient_descent():   #梯度下降
    times = 30
    study = 0.1
    x = 3
    y = 2
    for i in range(times):
        x = round(x - (2*x)*study,4)      #保留两位小数不可行
        y = round(y - (2*y)*study,4)
        z = round(z_number(x,y),2)             
        print(f'第{i+1}次迭代,此时:x = {x},y = {y},z = {z}')
if __name__ == "__main__":
    print(gradient_descent())        
for i in range(30):  
    print(i + 1)


'''自己写的'''
x = 3
y = 2
study = 0.1
f = fxy(x, y)
x = x - study*(2 * x)
y = y - study*(2 * y)







