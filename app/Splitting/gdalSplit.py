from osgeo import gdal
import numpy as np
import os
import cv2

def  split_tiff(img_path):


    xkm, ykm = (10, 10)               # BlockSize width(km), height(km)

    ds = gdal.Open(img_path)
    img = ds.ReadAsArray()
    shape = img.shape[1:] 
    img = np.dstack((img[2], img[1], img[0]))
    print("Image Loaded")

    gt = ds.GetGeoTransform()
    xs = gt[1]
    ys = gt[5]
    w, h = abs(round(xkm * 1000 / xs)), abs(round(ykm * 1000/ys))
    print("Width:", w, "Height:", h)

    dest_path = "app\Splitting\split_images\\"
    # os.chdir(dest_path)

    for i in range(0, shape[0], h):
        if i + h < shape[0]:
            for j in range(0, shape[1], w):
                imageName = dest_path + str(i//h) + "x" + str(j//w) + ".png"
                if j + w < shape[1]:
                    cv2.imwrite(imageName, img[i : i+h, j : j+w])
                else:
                    cv2.imwrite(imageName, img[i : i+h, j : ])
        else:
            for j in range(0, shape[1], w):
                imageName = dest_path +  str(i//h) + "x" + str(j//w) + ".png"
                if j + w < shape[1]:
                    cv2.imwrite(imageName, img[i : , j : j+w])
                else:
                    cv2.imwrite(imageName, img[i : , j : ])
    return imageName