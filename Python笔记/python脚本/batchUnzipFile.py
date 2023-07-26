import zipfile
import os
import shutil

def getZipFullPathSet():
    for root, dirs, files in os.walk(zip_dir):
        for file in files:
            if file.endswith("zip"):
                # print(os.path.join(root , file))
                zip_fullpath_set.add(
                    os.path.join(root, file))
    print(f"在文件夹{zip_dir}及其子目录下总共找到zip文件{len(zip_fullpath_set)}个")

def unzip(file_path):
    with zipfile.ZipFile(file_path, 'r') as zfile:
        for each in zfile.namelist():
            if each.endswith(".zip"):
                try:
                    zfile.extractall(path=out_dir, pwd=b"johngo_tec")
                    print("Extracted successfully")
                except Exception as e:
                    print(e)

def setDirRightName():
    '''
    使用zipfile解压文件名中文乱码，用此函数解决乱码
    :return:
    '''
    for root,dirs,files in os.walk(out_dir):
        for dirName in dirs:
            rightName = dirName.encode('cp437').decode('utf-8')
            dir = os.path.join(root, rightName)
            src = os.path.join(root, dirName)
            os.rename(src, dir)

def setFileRightName():
    for root,dirs,files in os.walk(out_dir):
        for fileName in files:
            if fileName.endswith(".zip"):
                rightName = fileName.encode('cp437').decode('utf-8')
                dir = os.path.join(root , rightName)
                src = os.path.join(root , fileName)
                os.rename(src , dir)






zip_dir = r"C:\Users\squir\Desktop\allZipFiles"
out_dir = r"C:\Users\squir\Desktop\解压目标文件夹"
zip_fullpath_set = set()
out_fullpath_set = set()

getZipFullPathSet()
for each in zip_fullpath_set:
    unzip(each)

setDirRightName()
setFileRightName()
















