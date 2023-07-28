import os
import numpy as np
import cv2
import glob

# Get the image directories
root = '..\\data\\caltech_crop_birds\\'
root = '../data/caltech_crop_birds/'
# data_dirs = glob.glob(root + '**/*.jpg', recursive=True)
# data_dirs = np.array(data_dirs)
# data_dirs = data_dirs.flatten()

dirs_file = open('../data/caltech_birds.txt', 'r')
raw_dirs = dirs_file.readlines()
data_dirs = [x.strip().split(' ')[1] for x in raw_dirs]

# roots = np.array([root] * len(data_dirs))
# data_dirs = np.core.defchararray.add(roots, data_dirs)

# Get the bbox locations
bbox_file = open('../data/caltech_labels.txt', 'r')
locs = bbox_file.readlines()

# file = open('test.txt','w')
# for item in data_dirs:
# 	file.write(item+"\n")
# file.close()

assert len(data_dirs) == len(locs)


# label_file = open('labels.txt', 'a')
for i in range(len(locs)):
    dir = data_dirs[i]
    print(dir)
    img = cv2.imread(root + dir)
    h, w, c = img.shape
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2.imshow('test', img)
    # cv2.waitKey(0)

    info = locs[i].strip().split(' ')
    info = [int(float(x)) for x in info]

    _, x, y, width, height = info

    if height > width:

        center_x = x + (width // 2)
        x_start = max(0, center_x - height // 2)
        x_end = min(w, center_x + height // 2)

        cropped = img[y:y+height, x_start:x_end, :]

        cv2.imwrite(root + dir, cropped)

    else:
        center_y = y + (height // 2)
        y_start = max(0, center_y - width // 2)
        y_end = min(h, center_y + width // 2)

        cropped = img[y_start:y_end, x:x+width, :]

        cv2.imwrite(root + dir, cropped)






    # cropped = cv2.resize(cropped, (128, 128))
    
    # cv2.imshow('test', img)
    # cv2.imshow('test2', cropped)
    # k = cv2.waitKey(0)

    # if k & 0xFF == ord('s'):
    #     label = 0
    # elif k & 0xFF == ord('f'): # skip the frame
    #     label = 1
    # else:
    #     label = -1

    # label_file.write(f'{dir} {label}\n')


    


# label_file.close()
    
