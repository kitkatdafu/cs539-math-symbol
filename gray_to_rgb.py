import cv2
import os
from shutil import copyfile

if 'yuanrgbimgs' not in os.listdir():
    os.mkdir('yuanrgbimgs')

for root, dirs, files in os.walk('yuanimgs'):
    for file in files:
        if file == '.DS_Store':
            continue
        file_path = os.path.join(root, file)
        gray_img = cv2.imread(file_path)
        rgb_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)
        cv2.imwrite(os.path.join('yuanrgbimgs', file), rgb_img)
