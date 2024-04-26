import torch
import torch.nn as nn
import torch.nn.functional as F

class AlexNet(nn.Module):
    '''
    接收输入图像size：227*227
    输出分类：num_classes为分类类别
    '''
    def __init__(self, num_classes=1000):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            # 对于卷积：stride默认值为1，padding默认值为0
            # 输入：227*227 输出：55*55
            nn.Conv2d(3, 96, kernel_size=11, stride=4, padding=0),
            nn.ReLU(inplace=True),
            # 输入：55*55 输出：27*27
            nn.MaxPool2d(kernel_size=3, stride=2),

            # 输入：27*27 输出：27*27
            nn.Conv2d(96, 256, kernel_size=5, stride=1 , padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(256, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )

        self.classifier = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(0.5),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

# 创建一个AlexNet模型实例
model = AlexNet(num_classes=1000)

# 打印模型结构
print(model)
