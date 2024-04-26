'''
傅里叶变换实验
'''
import numpy as np
import cv2
import os

from matplotlib import pyplot as plt

image_path = r'E:\background_group_2.jpg'


# 读取图像为灰度格式
image = cv2.imread(image_path, 0)

# 对图像进行傅里叶变换
dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# 获取图像中心位置
rows, cols = image.shape
crow, ccol = rows // 2 , cols // 2

# 创建低通滤波器掩码（中心圆形为1，其余为0）
rradius = 5    # 半径为100
mask = np.zeros((rows, cols, 2), np.uint8)
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= rradius**2
mask[mask_area] = 1

# 应用掩码并进行逆傅里叶变换
fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# 显示原始图像和滤波后的图像
plt.subplot(121), plt.imshow(image, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap = 'gray')
plt.title('Image after LPF'), plt.xticks([]), plt.yticks([])
plt.savefig(r'E:\Image_after_LPF_'+str(rradius)+'.jpg')
plt.show()

# # 保存滤波后的图像
# filtered_image_path = r'E:\Image_after_LPF_'+str(rradius)+'.jpg'  # 更新为保存路径
# cv2.imwrite(filtered_image_path, img_back)
