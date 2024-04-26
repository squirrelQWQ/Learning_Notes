import os
import sys
import torch.nn as nn
import torch.optim as optim
from torchvision import models
import time
from torchvision.models import ResNet101_Weights
from dataset.DataSet_LSM import DataSet_LSM
import torch
from torchvision import transforms
from torch.utils.data import DataLoader



# 加载数据集
def create_dataloaders(data_root_dir, split_code, batch_size , num_workers=4):
    # 定义数据预处理
    data_transforms = transforms.Compose([
        transforms.Resize(256),     # 先将图像大小调整为256x256
        transforms.CenterCrop(224), # 然后裁剪中心区域为224x224
        transforms.ToTensor(),      # 将图像转换为PyTorch张量
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # 标准化
    ])

    # 加载数据集
    train_dataset = DataSet_LSM(data_root_dir, transform=data_transforms, mode='train', split_code=split_code)
    test_dataset = DataSet_LSM(data_root_dir, transform=data_transforms, mode='test', split_code=split_code)
    val_dataset = DataSet_LSM(data_root_dir, transform=data_transforms, mode='validation', split_code=split_code)

    # 定义数据加载器
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)

    print("train数据规模:", len(train_dataset))
    print("test数据规模:", len(test_dataset))
    print("val数据规模:", len(val_dataset))

    return train_loader, test_loader, val_loader

def train_model(model, train_loader, test_loader, criterion, optimizer, num_epochs=10 , device='cuda'):
    for epoch in range(num_epochs):             # 一个轮次代表投喂模型所有的训练样本一轮
        model.train()  # 设置模型为训练模式
        running_loss = 0.0
        for inputs, labels in train_loader:     # 实际上训练过程中每投入一个批次的数据模型都进行了一次更新
            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()           # 梯度清零，防止上一个批次的梯度干扰这次更新

            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()         # 依据损失函数计算梯度（链式法则、计算图+自动求导）
            optimizer.step()        # 依据梯度和优化函数进行参数更新（比如随机梯度下降SGD等等）

            running_loss += loss.item()

        print(f"第 {epoch+1}轮train损失值为： {running_loss / len(train_loader)}")

        # 在验证集上检验模型
        model.eval()  # 设置模型为评估模式
        test_loss = 0.0
        correct = 0
        total = 0
        TP = 0  # 真正例
        FP = 0  # 假正例
        FN = 0  # 假负例
        TN = 0  # 真负例


        with torch.no_grad():
            for inputs, labels in test_loader:
                inputs, labels = inputs.to(device), labels.to(device)
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                test_loss += loss.item()

                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
                TP += ((predicted == 1) & (labels == 1)).sum().item()
                FP += ((predicted == 1) & (labels == 0)).sum().item()
                FN += ((predicted == 0) & (labels == 1)).sum().item()
                TN += ((predicted == 0) & (labels == 0)).sum().item()

        precision = TP / (TP + FP) if (TP + FP) > 0 else 0
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0
        F1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        print(f"第 {epoch + 1}轮test上损失值为：{test_loss / len(test_loader)}")
        print(f"第 {epoch + 1}轮test上TP为：{TP}")
        print(f"第 {epoch + 1}轮test上FP为：{FP}")
        print(f"第 {epoch + 1}轮test上FN为：{FN}")
        print(f"第 {epoch + 1}轮test上TN为：{TN}")
        print(f'第 {epoch + 1}轮test上准确率为：{100 * correct / total}%')
        print(f'第 {epoch + 1}轮test上召回率为：{100 * recall}%')
        print(f'第 {epoch + 1}轮test上F1分数为：{F1}')



# 用验证集来验证训练好的模型
def val_model(model, val_loader, criterion, device='cuda'):
    model.eval()  # 设置模型为评估模式
    val_loss = 0.0
    correct = 0
    total = 0
    TP = 0  # 真正例
    FP = 0  # 假正例
    FN = 0  # 假负例
    TN = 0  # 真负例

    with torch.no_grad():
        for inputs, labels in val_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            val_loss += loss.item()

            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            TP += ((predicted == 1) & (labels == 1)).sum().item()
            FP += ((predicted == 1) & (labels == 0)).sum().item()
            FN += ((predicted == 0) & (labels == 1)).sum().item()
            TN += ((predicted == 0) & (labels == 0)).sum().item()

    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    F1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    print(f"在验证集上的TP为：{TP}")
    print(f"在验证集上的FP为：{FP}")
    print(f"在验证集上的FN为：{FN}")
    print(f"在验证集上的TN为：{TN}")
    print(f"验证集损失为：{val_loss / len(val_loader)}")
    print(f'在验证集上的准确率为：{100 * correct / total}%')
    print(f'在验证集上的召回率为：{100 * recall}%')
    print(f'在验证集上的F1分数为：{F1}')

def main():
    # 加载数据集
    # data_root_dir = '/data/cwj_workspace/LSM'
    data_root_dir = r'E:\Dataset\LSM\mark_checked'
    split_code = 42
    batch_size = 16
    train_loader, test_loader, val_loader = create_dataloaders(data_root_dir, split_code , batch_size)

    # 设置设备
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # 加载预训练模型
    # model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
    # model = model.to(device)
    # print("使用的模型为resnet50")
    model = models.resnet101(weights=ResNet101_Weights.IMAGENET1K_V1)
    model = model.to(device)
    print("使用的模型为resnet101")

    # 定义学习率、训练轮次、损失函数和优化器
    lr = 0.001
    num_epochs = 20
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)


    # 记录开始时间
    start_time = time.time()

    # 训练和测试模型
    train_model(model, train_loader, test_loader, criterion, optimizer, num_epochs , device)

    # 计算总时间（秒）转换为小时和分钟
    end_time = time.time()
    total_time_seconds = end_time - start_time
    hours = int(total_time_seconds // 3600)
    minutes = int((total_time_seconds % 3600) // 60)
    print(f"训练总共耗费时间: {hours} 小时, {minutes} 分钟")


    # 用验证集验证模型
    val_model(model, val_loader, criterion , device)

if __name__ == '__main__':
    main()


'''
# # 查看数据集的信息
# def print_dataset_info(dataset, name):
#     print(f"Information for {name}:")
#     print(f"数据集大小: {len(dataset)}")
# 
#     # 尝试获取第一个样本
#     if len(dataset) > 0:
#         first_image, first_label = dataset[0]
#         print(f"Example of image size: {first_image.size()}")
#         print(f"Example of label: {first_label}")
# 
#     # 如果数据集包含类别标签，可以进一步分析类别分布
#     if hasattr(dataset, 'labels'):
#         from collections import Counter
#         label_counts = Counter(dataset.labels)
#         print(f"不同类型标签数目统计: {label_counts}\n\n")
# 
# # 使用定义的函数打印每个数据集的信息
# print_dataset_info(LSM_Dataset_train, "Training Dataset")
# print_dataset_info(LSM_Dataset_test, "Testing Dataset")
# print_dataset_info(LSM_Dataset_val, "Validation Dataset")


# # 验证集之间是否有重叠
# def check_for_overlap(datasets, dataset_names):
#     dataset_ids = [set(dataset.images) for dataset in datasets]  # 假设图像路径存储在 images 属性中
#     for i in range(len(datasets)):
#         for j in range(i + 1, len(datasets)):
#             overlap = dataset_ids[i].intersection(dataset_ids[j])
#             if overlap:
#                 print(f"数据集 {dataset_names[i]} and {dataset_names[j]}之间有重叠的数据: {len(overlap)} items")
#             else:
#                 print(f"数据集 {dataset_names[i]} and {dataset_names[j]}之间没有重叠")
# 
# # 调用函数检查训练集、测试集和验证集之间是否有重叠
# check_for_overlap(
#     [LSM_Dataset_train, LSM_Dataset_test, LSM_Dataset_val],
#     ["Training Dataset", "Testing Dataset", "Validation Dataset"]
# )
'''


'''
# 数据集路径
data_root_dir = 'E:\Dataset\LSM\mark_checked'
split_code = 42 # 随机数种子，用于数据集切割

# 定义数据预处理
data_transforms = transforms.Compose([
    transforms.Resize(256),     # 先将图像大小调整为256x256（短边缩放至256，长边同比例缩放）
    transforms.CenterCrop(224), # 然后裁剪中心区域为224x224
    transforms.ToTensor(),      # 将图像转换为PyTorch张量
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # 标准化，这里的参数是imagenet数据集得来的经验值
])

# 加载数据集
LSM_Dataset_train = DataSet_LSM(data_root_dir, transform=data_transforms, mode='train' , split_code=split_code)
LSM_Dataset_test = DataSet_LSM(data_root_dir, transform=data_transforms, mode='test' , split_code=split_code)
LSM_Dataset_val = DataSet_LSM(data_root_dir, transform=data_transforms, mode='validation' , split_code=split_code)
# 定义数据加载器
train_loader = DataLoader(LSM_Dataset_train, batch_size=32, shuffle=True, num_workers=4)
test_loader = DataLoader(LSM_Dataset_test, batch_size=32, shuffle=True, num_workers=4)
val_loader = DataLoader(LSM_Dataset_val, batch_size=32, shuffle=False, num_workers=4)
'''






