import torch
import torch.nn as nn
import torch.nn.functional as F

class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        # 定义卷积层
        self.conv1 = nn.Conv2d(1, 6, 5) # 输入通道1, 输出通道6, 卷积核大小5x5
        self.conv2 = nn.Conv2d(6, 16, 5) # 输入通道6, 输出通道16, 卷积核大小5x5
        # 定义全连接层
        self.fc1 = nn.Linear(16*4*4, 120) # 16*4*4 输入特征数, 120 输出特征数
        self.fc2 = nn.Linear(120, 84) # 120 输入特征数, 84 输出特征数
        self.fc3 = nn.Linear(84, 10) # 84 输入特征数, 10 输出特征数 (数字0-9)


    def forward(self, x):
        # 卷积 -> 激活 -> 池化
        # size:64*1*28*28
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2)) # 使用2x2的窗口进行最大池化
        # size:64*6*12*12
        x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2)) # 使用2x2的窗口进行最大池化
        # size:64*16*4*4
        # print(x.size())
        x = x.view(-1, self.num_flat_features(x)) # 展平多维的卷积图特征，准备全连接层处理
        # size:64*256
        # print(x.size())
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        x = F.softmax(x , dim=1)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:] # 除批量维度外的所有维度
        num_features = 1
        for s in size:
            num_features *= s
        return num_features

# # 使用LeNet
# net = LeNet()
# print(net)

