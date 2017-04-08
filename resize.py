import cv2
import numpy as np
import os

obj = raw_input("Please input the object name:")
num = 0

if not os.path.exists("resized/%s/" % obj):
    os.makedirs("resized/%s/" % obj)

for image in os.listdir("images/%s/" % obj):
    img = cv2.imread(("images/%s/") % obj + image)
    re_img = cv2.resize(img, (512, 512))
    cv2.imwrite(("resized/%s/" + str(num) + ".jpg") % obj, re_img)
    num += 1
    print(image + ' resized over')
