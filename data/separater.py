import os
import cv2
import time

dir_path = "../data_raw"

dic = {"Air": "cam0", "Earth": "cam1", "Fire": "cam2", "Water": "cam3"}
dirs = os.listdir(dir_path)
# print(dirs)

for dir_name in dirs:
    # print(dir_name)
    if os.path.isdir(os.path.join(dir_path, dir_name)):
        cam_names = dir_name.split("_")
        cam_dir = [os.path.join(".", dic[cam_names[i]]) for i in range(len(cam_names))]
        # print(cam_dir)
        for i in range(len(cam_dir)):
            # print(cam_dir[i])
            if not os.path.exists(cam_dir[i]):
                os.mkdir(cam_dir[i])
        # print((os.path.isdir(os.path.join(dir_path, dir_name)))

        for img_file in os.listdir(os.path.join(dir_path, dir_name)):
            img = cv2.imread(os.path.join(dir_path, dir_name,img_file))
            # print(img_file)
            img2 = img

            height, width, channels = img.shape

            for i in range(len(cam_dir)):
                x = int(width/2 * i)
                y = 0
                h = height
                w = int(width / 2)
                # print(x,y, x+w, y+h)
                img = img[y:y+h, x:x+w]

                filename = dir_name + "_" + img_file[-6:]
                NAME = os.path.join(cam_dir[i], filename) 
                cv2.imwrite(NAME,img)
                img = img2