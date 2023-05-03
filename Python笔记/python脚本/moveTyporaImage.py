'''
    整个脚本是由chatGPT写的，我只进行了些许修改
'''

import os
import re
import shutil
from bs4 import BeautifulSoup


# 定义正则表达式用于匹配.md文件中的图片引用语句
pattern = re.compile(r'!\[.*]\((.*)\)')

# 获取所有.md文件中的图片引用路径
references = set()
md_filepath = input("请输入 Markdown 文件所在目录的路径: ")
# md_filepath = r'{}'.format(md_filepath)

for file in os.listdir(md_filepath):
    if file.endswith('.md'):            # 扫描该路径下的所有.md文件，并查找其中的图片
        with open(os.path.join(md_filepath, file), 'r', encoding='utf-8') as f:
            text = f.read()
            references.update(pattern.findall(text))
            soup = BeautifulSoup(text, 'html.parser')
            for img in soup.find_all('img'):
                src = img.get('src')
                if src:
                    references.add(os.path.join(md_filepath, src))

print(f"在此路径中的所有.md文件中总共找到引用图片{len(references)}张")
usedImages = set()
for each in references:
    usedImages.add(each.split('/')[1])


# 获取.assets目录的路径
assets_filepath = input("请输入.assets目录的路径: ")

# 遍历.assets目录中的所有文件，将未被引用的图片移动到 delete 目录中
if not os.path.exists(os.path.join(assets_filepath, 'delete')):
    os.mkdir(os.path.join(assets_filepath, 'delete'))

allImageNum = 0
deleteNum = 0
for file in os.listdir(assets_filepath):
    allImageNum += 1
    # print(file)
    if file not in usedImages:
        shutil.move(os.path.join(assets_filepath, file), os.path.join(assets_filepath, 'delete'))
        print(f"移动图片{file}到delete文件夹中")
        deleteNum += 1

print(f"assert文件夹中总共有图片{allImageNum}张\n总共移动{deleteNum}张图片到delete中")

    # 输入示例
    # C:\Users\squir\Desktop\学习笔记\Git笔记
    # C:\Users\squir\Desktop\学习笔记\Git笔记\Git笔记.assets

    # C:\Users\squir\Desktop\学习笔记\MySQL笔记
    # C:\Users\squir\Desktop\学习笔记\MySQL笔记\MySQL笔记.assets

