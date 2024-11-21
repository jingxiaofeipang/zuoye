import numpy as np

# 激活函数：sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 神经网络类
class SimpleNN:
    def __init__(self):
        # 初始化权重和偏置
        self.weight = 1.0  # 权重
        self.bias = -2.0  # 偏置

    def predict(self, input_data):
        # 计算输出
        output = sigmoid(np.dot(input_data, self.weight) + self.bias)
        return output

# 创建神经网络实例
nn = SimpleNN()

# 模拟一个输入，代表数字“1”
# 这里我们使用一个6位的二进制数，只有一个位是1，其余都是0
# 例如，第3位是1，可以模拟一个简单的“1”形状
input_data = np.array([0, 0, 1, 0, 0, 0])

# 使用神经网络进行预测
output = nn.predict(input_data)

# 根据输出结果判断是否识别为数字“1”
# 如果输出大于0.5，我们可以认为网络识别出了数字“1”
if output > 0.5:
    print("The neural network recognizes the input as the digit 1.")
else:
    print("The neural network does not recognize the input as the digit 1.")