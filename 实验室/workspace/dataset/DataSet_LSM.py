import os
from PIL import Image
import pandas as pd
from torch.utils.data import Dataset
from torchvision.transforms import transforms
from sklearn.model_selection import train_test_split


class DataSet_LSM(Dataset):
    def __init__(self, root_dir, transform=None, mode="train" , split_code=42):
        '''
        初始化 LSM_Dataset 类

        参数：
            - root_dir (str)：数据集根目录路径
            - transform (callable, optional)：数据转换操作
            - mode (str, optional)：指示数据集模式('train', 'test', 'validation')，训练、测试、验证
            - split_code 一个随机数用于确定数据划分规则

        root_dir 下的文件目录结构如下：
        LSM/
        ├── LS002/
        │   ├── image1.jpg
        │   ├── image2.jpg
        │   └── ...
        ├── LS003/
        │   └── ...
        └── ...

        初始化数据集，并加载数据集中的图像文件路径和标签

        '''

        self.root_dir = root_dir
        self.transform = transform
        self.mode = mode

        self.folders = sorted(os.listdir(root_dir))     #按字典序获取root_dir下的文件夹(比如：LS002)
        print(f"正在加载{mode}数据")
        print("在"+root_dir+"下找到如下文件夹：\n",self.folders)

        self.images = []  # 存储图像文件路径
        self.labels = []  # 存储图像标签

        # 先在图像所在文件夹下找到csv标签文件，获得字典{img_name:label}
        for each_folder in self.folders:
            print("正在处理文件夹：", each_folder)
            folder_dir = os.path.join(root_dir, each_folder)
            csv_file = ""
            files = os.listdir(folder_dir)
            for file in files:
                if file.lower().endswith('.csv'):
                    csv_file = os.path.join(folder_dir, file)
            lable_dict = self.get_label_dict(csv_file)      # 获取标签字典{img_name:label}

            # 存储文件所在路径和对应标签
            for each_img in os.listdir(folder_dir):
                if each_img.lower().endswith('.jpg'):
                    img_path = os.path.join(folder_dir, each_img)
                    self.images.append(img_path)
                    self.labels.append(lable_dict[each_img])

        # 分割数据集
        X_train, X_temp, y_train, y_temp = train_test_split(self.images, self.labels, test_size=0.2,
                                                                        random_state=split_code)
        X_test, X_val, y_test, y_val = train_test_split(X_temp, y_temp, test_size=0.5, random_state=split_code)
        if self.mode == 'train':
            self.images = X_train
            self.labels = y_train
        elif self.mode == 'test':
            self.images = X_test
            self.labels = y_test
        elif self.mode == 'validation':
            self.images = X_val
            self.labels = y_val
        print(f"{mode}数据集获取完毕\n")

    def __len__(self):
        '''
        返回数据集的长度
        '''
        return len(self.images)

    def __getitem__(self, idx):
        '''
        根据索引获取数据集中的样本

        参数：
            - idx (int)：样本的索引

        返回：
            - sample (tuple)：包含图像和标签的元组
        '''
        image_path = self.images[idx]  # 获取指定索引处的图像文件路径
        label = self.labels[idx]  # 获取指定索引处的图像标签

        image = Image.open(image_path).convert('RGB')  # 读取图像并转换为RGB格式
        if self.transform:  # 如果指定了转换操作
            image = self.transform(image)  # 对图像进行转换操作

        return image, label  # 返回图像和标签的元组

    def get_label_dict(self , csv_file):
        '''
        读取csv文件，返回数据标签字典列表
        图片非空为1，图片空为0
        '''

        df = pd.read_csv(csv_file , encoding='GBK')        # 读取 CSV 文件
        label_dict = {}     # 创建字典，存储 name-label 对应关系

        for index, row in df.iterrows():
            tag1_exists = pd.notnull(row['tag1'])     # 检查 'tag1' 和 'tag2' 列是否有不为空的值
            tag2_exists = pd.notnull(row['tag2'])
            label = 1 if tag1_exists or tag2_exists else 0  # 如果 'tag1' 或 'tag2' 列有不为空的值，标记为 1；否则标记为 0
            label_dict[row['name']] = label           # 将图像名称和标签存储到字典中
        return label_dict

