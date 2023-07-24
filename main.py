import os
import ImgTextClipboard
import numpy as np
import cv2

from PIL import Image


def main():
    # 读取剪贴板图片
    img = ImgTextClipboard.copyImgFormClipboard()
    # Image转cv2
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    # 缩放图片判断 单位 MB
    while getCv2ImgDataSize(img) > 10:
        # 图像信息获取
        img_stats = img.shape
        dst_width = int(img_stats[0] * 0.9)
        dst_height = int(img_stats[1] * 0.9)

        img = cv2.resize(img, (dst_height, dst_width))

    # cv2转Image
    img = Image.fromarray(cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB))
    # 粘贴图片
    ImgTextClipboard.pasteImgToClipboard(img)


def getCv2ImgDataSize(img):
    # 临时生成图片路径
    temp_path = './temp.png'
    # 输出图片
    cv2.imwrite(temp_path, img)
    stats = os.stat(temp_path)
    # 删除临时图片
    os.remove(temp_path)
    return stats.st_size / 1024 / 1024


if __name__ == '__main__':
    main()
