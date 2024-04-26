import os

import torch
import torch.nn as nn
from matplotlib import pyplot as plt
from matplotlib.pyplot import plot
from torchvision import transforms
from PIL import Image

from CNN.LeNet import LeNet

# 加载模型
net = LeNet()
net.load_state_dict(torch.load('../pth/LeNet_lr_0.001_epochs_10_2024-04-02_10-12-46.pth'))
# 设为评估模式
net.eval()


def predict_images_in_folder(folder_path, model):
    """
    对指定文件夹中的所有图像进行预测。

    参数:
        folder_path (str): 包含图像的文件夹的路径。
        model (torch.nn.Module): 已训练的PyTorch模型。

    返回:
        dict: 一个字典，键为图像文件名，值为预测的类别。
    """
    # 确保模型处于评估模式
    model.eval()

    # 定义与训练相同的预处理操作
    transform = transforms.Compose([
        transforms.Resize((28, 28)),  # 假设输入尺寸为28x28
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))  # 标准化
    ])

    predictions = {}
    # 遍历文件夹中的所有文件
    image_names = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png','.jpg','.jpeg','.bmp'))]
    for filename in image_names:
        file_path = os.path.join(folder_path, filename)
        # 确保是文件而不是文件夹
        if os.path.isfile(file_path):
            # 加载图片并转为灰度图像
            image = Image.open(file_path).convert('L')

            # 应用预处理
            image = transform(image)

            image = image.unsqueeze(0)  # 增加一个批量维度

            # 不计算梯度
            with torch.no_grad():
                outputs = model(image)
                print(outputs)
                _, predicted = torch.max(outputs, 1)
                predictions[filename] = predicted.item()

    return predictions


# 使用函数对文件夹下的所有图像进行预测
folder_path = r'C:\Users\squir\Desktop\实验室\model\data\手写数字'
predictions = predict_images_in_folder(folder_path, net)
for filename, predicted_class in predictions.items():
    print(f'文件名: {filename}, 预测类别: {predicted_class}')