import cv2

import os,glob

from os import listdir,makedirs

from os.path import isfile,join
for i in range (1,51):
    path = r"F:\\Dataset\\Image frames\\Name"+str(i)  # Source Folder
    #"F:\Dataset\Image frames\POSE\S1\C\90"
    dstpath = "F:\\Dataset\\Image frames\\NewName"+str(i)  # Destination Folder
    try:
        makedirs(dstpath)
    except:
        print ("Directory already exist, images will be written in same folder S" +str(i))

    files = os.listdir(path)

    for image in files:
        img = cv2.imread(os.path.join(path,image))
        #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)             # Optional to covert all images in binary format
        cv2.imwrite(os.path.join(dstpath,image))
