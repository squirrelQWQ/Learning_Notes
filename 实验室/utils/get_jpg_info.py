import random
import shutil

from PIL import Image
import os
import csv

# 指定你的图片文件夹路径
# folder_path = '/data/utils/LS006'
folder_path = r'E:\数据集\LS006'
# 指定输出CSV文件的路径
csv_file_path = r'E:\数据集\LS006\统计.csv'

def determine_day_night(image_path):
    '''
    1.由于LSM数据集中图像都是 sRGB 表示，但是夜晚拍摄的图像表现出灰度（r=g=b） 故由此判断图像是白天拍摄还是晚上拍摄
    2.随机选取1000个像素点，加速运算过程
    :param image_path:
    :return:
    '''
    with Image.open(image_path) as img:
        # 将图像转换为RGB（确保处理的是RGB图像）
        img = img.convert('RGB')

        # 随机取1000个像素点判断它的rgb值
        width, height = img.size
        num_pixels = 1000
        day_count = 0

        for _ in range(num_pixels):
            # 生成一个随机坐标
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            # 获取该坐标的像素值
            r, g, b = img.getpixel((x, y))
            # 统计像素点不是灰度表示的个数，大于20认为是白天拍摄的
            if r != g != b:
                day_count += 1
        if day_count > 20:
            return "Day"
        return "Night"


def write_2_csv(folder_path , csv_file_path):
    '''
    将folder_path下所有jpg图像的信息都写入csv_file_path文件中
    :return:
    '''
    # 准备写入CSV文件
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # 写入标题行
        writer.writerow(['Filename', 'Size (Bytes)', 'Day/Night', 'width', 'height'])

        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.lower().endswith('.jpg'):
                    # 构建文件的完整路径
                    file_path = os.path.join(folder_path, filename)
                    # print(filename)
                    # 获取文件大小
                    size = os.path.getsize(file_path)
                    # 判断是白天还是夜晚
                    day_night = determine_day_night(file_path)
                    # 打开图片以获取分辨率
                    with Image.open(file_path) as img:
                        width = img.width
                        height = img.height

                    # 写入一行数据
                    writer.writerow([filename, size, day_night, width, height])

    print(f'信息已保存到 {csv_file_path}')




def backup_images_Day_Night(folder_path):
    '''
    把图像备份一份分别放在Day和Night文件夹下
    :param folder_path:
    :return:
    '''
    # 在当前路径下创建Day和Night两个文件夹
    day_path = os.path.join(folder_path, "Day")
    night_path = os.path.join(folder_path, "Night")

    if not os.path.exists(day_path):
        os.makedirs(day_path)
    if not os.path.exists(night_path):
        os.makedirs(night_path)

    day_num = 0
    night_num = 0
    # 遍历folder_path下的所有图像文件
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg')):  # 检查文件扩展名
            image_path = os.path.join(folder_path, filename)

            # 使用你的函数判断是Day还是Night
            if determine_day_night(image_path) == "Day":
                # 复制到Day文件夹
                shutil.copy(image_path, day_path)
                day_num += 1
            else:
                # 复制到Night文件夹
                shutil.copy(image_path, night_path)
                night_num += 1
    print("Day中图片共有"+str(day_num)+"张")
    print("Night中图片共有"+str(night_num)+"张")


write_2_csv(folder_path , csv_file_path)
backup_images_Day_Night(folder_path)
