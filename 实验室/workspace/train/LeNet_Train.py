import time

import torch
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim
from torch import nn

from CNN.LeNet import LeNet

# 1. 数据加载
# MNIST中图像为（1，28，28）
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
trainset = torchvision.datasets.MNIST(root='../data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)    # 60000张

testset = torchvision.datasets.MNIST(root='../data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False) # 10000张

# 2. 模型实例化
net = LeNet()

# 超参数
epochs = 10
lr = 0.001


# 3. 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=lr, momentum=0.9)



# 4. 训练模型
# 遍历数据集10次，每次遍历称为一个epoch
for epoch in range(epochs):
    # 初始化累计损失
    running_loss = 0.0

    # enumerate(trainloader, 0)遍历训练数据加载器，trainloader加载了训练数据
    # i是批次计数器，data是包含图像和标签的批次数据
    for i, data in enumerate(trainloader, 0):
        # 解包data，获取当前批次的输入图像和对应的标签
        inputs, labels = data

        # 在每次的参数更新前清零累积的梯度，防止梯度在多次backward()调用时累积
        optimizer.zero_grad()

        # 前向传播：将输入数据喂给网络，计算网络输出
        outputs = net(inputs)  # 假设 inputs 是 64 * 1 * 28 * 28，即批量大小为64，单通道28x28像素图像

        # 计算损失：比较网络输出和真实标签，计算损失值
        loss = criterion(outputs, labels)

        # 反向传播：根据损失计算梯度
        loss.backward()

        # 优化步骤：更新网络参数
        optimizer.step()

        # 累计损失
        running_loss += loss.item()

        # # 每遍历200个批次，打印一次日志
        # if i % 200 == 199:  # i是从0开始的，所以i % 200 == 199表示每200次迭代
        #     # 打印当前epoch，批次编号，以及这200个批次的平均损失
        #     print(f'[{epoch + 1}, {i + 1}] loss: {running_loss / 200:.3f}')
        #     # 重置累计损失，为下一个200个批次的损失统计做准备
        #     running_loss = 0.0

print('Finished Training')

current_timestamp = time.time()
current_time = time.localtime(current_timestamp)
current_datatime = time.strftime("%Y-%m-%d_%H-%M-%S", current_time)
# 定义文件名，包含学习率和训练轮次
model_path = f"../pth/LeNet_MNIST_lr_{lr}_epochs_{epochs}_{current_datatime}.pth"
torch.save(net.state_dict(), model_path)

# # 5. 测试模型
# correct = 0
# total = 0
# # 不计算梯度，用于节省计算资源，加速推理过程
# with torch.no_grad():
#     # 遍历测试数据集
#     for data in testloader:
#         # 解包数据，获取当前批次的图像和标签
#         images, labels = data
#
#         # 将当前批次的图像输入模型，获得预测结果
#         outputs = net(images)
#
#         # torch.max 返回每一行的最大值及其索引
#         # outputs.data是获取模型输出的tensor数据
#         # 1表示在哪一个维度上寻找最大值，这里的1代表列，即对每一行找到最大值，返回最大值的索引
#         # predicted是预测的类别标签
#         _, predicted = torch.max(outputs.data, 1)
#
#         # labels.size(0)返回当前批次的样本数，累加到总样本数中
#         total += labels.size(0)
#
#         # (predicted == labels).sum().item()计算当前批次中预测正确的样本数
#         # predicted == labels 返回一个布尔值数组，表示预测是否正确
#         # .sum()计算数组中True的个数（即预测正确的数量）
#         # .item()将这个数转换为Python的标量
#         # 累加到correct中，表示总的正确预测数
#         correct += (predicted == labels).sum().item()
#
# # 最终，correct变量存储了整个测试集中正确预测的样本数，total变量存储了测试集的总样本数
#
#
# print(f'Accuracy of the network on the 10000 test images: {100 * correct / total} %')
