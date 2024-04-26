import time
from PIL import Image
import numpy as np
import os

def calculate_background(folder_path:str, group_size:int=None):
    '''
    从night文件夹中的图像计算背景图像
    已经检查过，LSM数据的大小都是统一的4000x3000,所以无需进行大小的检查，直接就可以生成背景图
    :param folder_path:图像所在路径
    :param group_size:分组生成背景图，组的大小
    :return:
    '''
    if not os.path.exists(folder_path):
        print("输入的图像路径不存在")
        return
    # 背景图像保存的路径
    background_path = os.path.join(folder_path, "background_group"+str(group_size))

    if not os.path.exists(background_path):
        os.makedirs(background_path)
        print("文件夹"+background_path+"已创建")

    # 获取所有图像文件名
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]

    # 分组图像文件名
    groups = [image_files[i:i + group_size] for i in range(0, len(image_files), group_size)]

    # 为每一组图像计算并保存背景图像
    for group_idx, group in enumerate(groups, start=1):
        images = []
        for image_file in group:
            image_path = os.path.join(folder_path, image_file)
            img = Image.open(image_path)
            images.append(np.array(img))

        # 计算像素点值的平均值
        avg_image = np.mean(images, axis=0).astype(np.uint8)

        # 将平均后的数组转换回图像
        bg_image = Image.fromarray(avg_image)
        save_path = os.path.join(background_path, f"background_group_{group_idx}.jpg")
        bg_image.save(save_path)
        print(f"文件 {save_path} 已经保存")


# folder_path = r'E:\数据集\LS006\night'
# folder_path = r'E:\数据集\LS006\day'
folder_path = '/data/utils/LS006/Night'

num = 10
while num < 151:
    start_time = time.time()
    calculate_background(folder_path , group_size=num)
    end_time = time.time()  # 结束时间
    elapsed_time = end_time - start_time  # 计算经过时间

    print(f"处理 {num} 张图片计算背景所需的时间：{elapsed_time:.2f}秒。")
    num += 10



