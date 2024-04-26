# Modify the provided DataSet_LSM class to handle train, test, and validation splits
# modified_dataset_code =
import os
from PIL import Image
import pandas as pd
from torch.utils.data import Dataset
from torchvision.transforms import transforms
from sklearn.model_selection import train_test_split

class LSM_Dataset(Dataset):
    def __init__(self, root_dir, transform=None, mode='train'):
        '''
        初始化 LSM_Dataset 类

        参数：
            - root_dir (str)：数据集根目录路径
            - transform (callable, optional)：数据转换操作
            - mode (str, optional)：指示数据集模式('train', 'test', 'validation')

        root_dir 下的文件目录结构如下：
        LSM/
        ├── LS002/
        │   ├── image1.jpg
        │   ├── image2.jpg
        │   └── ...
        ├── LS003/
        │   └── ...
        └── ...

        文件列表和对应的标签需要在一个CSV文件中定义，例如 'labels.csv'。
        '''
        self.root_dir = root_dir
        self.transform = transform
        self.mode = mode
        self.data_info = pd.read_csv(os.path.join(root_dir, 'labels.csv'))
        self.train_data, temp_data = train_test_split(self.data_info, test_size=0.2, random_state=42)
        self.validation_data, self.test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

        if mode == 'train':
            self.data_info = self.train_data
        elif mode == 'test':
            self.data_info = self.test_data
        elif mode == 'validation':
            self.data_info = self.validation_data

    def __len__(self):
        return len(self.data_info)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, self.data_info.iloc[idx, 'image_path'])
        image = Image.open(img_name)
        if self.transform:
            image = self.transform(image)
        label = self.data_info.iloc[idx, 'label']
        return image, label


# Displaying the modified code snippet
print(modified_dataset_code[:1500])  # Displaying a part of the modified code to keep it manageable in size
