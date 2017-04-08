import cv2
import numpy as np
import os

obj = 'pencil'
num = 0
# print(os.listdir('images/' + obj + '/'))
for image in os.listdir("images/%s/" % obj):
    img = cv2.imread(("images/%s/") % obj + image)
    re_img = cv2.resize(img, (1024, 1024))
    cv2.imwrite(("resized/%s/" + str(num) + ".jpg") % obj, re_img)
    num += 1
    print(image + ' over')
