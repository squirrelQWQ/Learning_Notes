'''
    移动typora中assets文件夹中没有被引用的图片
'''

import os, re
import shutil
def getUsedNameSet():
    '''
        1.读取.md文件
        2.获得所有已经使用了的图片名
    :return: 返回已使用图片名字的集合
    '''
    # src = input("请输入待扫描.md文件完整完整名称：")
    with open(r'C:\Users\squir\Desktop\学习笔记\Git笔记\Git笔记.md', 'r' , encoding='utf-8') as md:
        for line in md:
            match = re.match("!\[]\((.*)\)" , line)
            if(match):
                name = match.group()[4:-1]
                usedNameSet.add(name.split(".assets/")[1])
    print(f"扫描到已引用图片：{len(usedNameSet)}张")

def getAssetsImages():
    '''
        1.读取assert文件中所有图片名
        2.依次判断图片是否被引用
            若引用则移到delete文件夹中
            若未引用则不做改动
    :return:返回移动的图片数目
    '''
    for root, dirs, files in os.walk(r"C:\Users\squir\Desktop\学习笔记\Git笔记\Git笔记.assets", topdown=False):
        for each in files:
            allNameSet.add(each)
    print(f"扫描到assets文件中图片：{len(allNameSet)}张")

def mkdir(path):
    '''
    创建文件夹
    :param path:
    :return:
    '''
    folder = os.path.exists(path)
    if not folder:              # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)       # makedirs 创建文件时如果路径不存在会创建这个路径
        print("创建新文件夹")
    else:
        print("文件夹已存在，无需创建")


def deleteImage():
    '''
        找到未引用的图片并执行删除操作
    :return: 没有返回值
    '''
    num = 0
    for each in allNameSet:
        if(each not in usedNameSet):
            num += 1
            src = os.path.join(r"C:\Users\squir\Desktop\学习笔记\Git笔记\Git笔记.assets" , each)
            dst = os.path.join(r"C:\Users\squir\Desktop\学习笔记\Git笔记\Git笔记_imageDelet", each)
            print(f"src:{src}")
            print(f"dst:{dst}")
            shutil.move(src , dst)
    print(f"总共移动图片{num}张")



def remove_file():

    for file in filelist:
        src = os.path.join(old_path, file)
        dst = os.path.join(new_path, file)
        print('src:', src)
        print('dst:', dst)
        shutil.move(src, dst)


usedNameSet = set()
allNameSet = set()


getUsedNameSet()
getAssetsImages()
path = r"C:\Users\squir\Desktop\学习笔记\Git笔记\Git笔记_imageDelet"
mkdir(path)  # 调用函数

deleteImage()








