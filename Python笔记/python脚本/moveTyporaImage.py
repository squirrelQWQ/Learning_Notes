'''
    移动typora中assets文件夹中没有被引用的图片
'''

import os
import re
import shutil


def getUsedNameSet():
    '''
        1.读取.md文件
        2.获得所有已经使用了的图片名
    :return: 返回已使用图片名字的集合
    '''
    # src = input("请输入待扫描.md文件完整完整名称：")
    with open(mdPath, 'r', encoding='utf-8') as md:
        for line in md:
            match = re.match("(.*)!\[(.*)]\((.*)\)(.*)", line)
            if (match):
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
    for root, dirs, files in os.walk(assetsPath, topdown=False):
        for each in files:
            allNameSet.add(each)
    print(f"扫描到assets文件中图片：{len(allNameSet)}张")

def getDeletePath():
    dir = os.path.split(mdPath)[0]
    name = os.path.split(mdPath)[1]
    str = f"{name[:-3]}_imageDelete"
    return os.path.join(dir, str)  # 拼接出新文件夹的路径名

def mkdir():
    '''
    创建文件夹
    :param path:
    :return:
    '''
    if not os.path.exists(deletePath):                  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(deletePath)                         # makedirs 创建文件时如果路径不存在会创建这个路径
        print(f"多余的图片将会放到新建的文件夹：{deletePath}")
    else:
        print(f"多余的图片将会放到文件夹：{deletePath}")


def deleteImage():
    '''
        找到未引用的图片并执行删除操作
    :return: 没有返回值
    '''
    num = 0
    for each in allNameSet:
        if (each not in usedNameSet):
            num += 1
            src = os.path.join(assetsPath, each)
            dst = os.path.join(deletePath, each)
            shutil.move(src, dst)
    print(f"总共移动图片{num}张")


def remove_file():
    for file in filelist:
        src = os.path.join(old_path, file)
        dst = os.path.join(new_path, file)
        shutil.move(src, dst)



print(r"路径名示例：C:\图片删除测试.md")
mdPath = input("请输入.md文件的完整路径：")
assetsPath = os.path.join(os.path.split(mdPath)[0] , f"{os.path.split(mdPath)[1][:-3]}.assets") # 默认.md文件和.assets文件在同一个目录下
# assetsPath = input("请输入.assets文件的完整路径：")

print("**************************************************************")
deletePath = getDeletePath()
print(deletePath)
mkdir()     # 创建未引用图片要存放的目录

usedNameSet = set()  # md文件中引用的图片名
allNameSet = set()  # assets文件中所有图片名

getUsedNameSet()
getAssetsImages()

deleteImage()
print("**************************************************************")