#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import csv
import os
from PIL import Image
from yolo import YOLO

save_dir    = '/media/zyzhong/Data/data3/HualuCUP/result/'
test_dir    = '/media/zyzhong/Data/data3/HualuCUP/ehualu/test_a/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

img_list = os.listdir(test_dir)
img_list = sorted(img_list)
total = len(img_list)
print(('testing images = %d' % total))
remain = total
start_time = time.time()

save_csv_path = os.path.join(save_dir, 'result.csv')
csvfile = open(save_csv_path, 'w')
writer = csv.writer(csvfile)
writer.writerow(['name', 'coordinate'])
yolo = YOLO()

'''
img_name = '0a9b09fc-632d-4051-a568-bc89049927d1.jpg'
img_path = os.path.join(test_dir + img_name)
'''
for i, img_name in enumerate(img_list):
    img_path = os.path.join(test_dir, img_name)
    img = img_path
    image = Image.open(img_path)
    predicted_class, score, x, y, w, h = yolo.detect_image(image)
    number = len(predicted_class)
    coordinate = ''    
    for i in range(number):
        if predicted_class[i] == 'car':
            coordinate = coordinate + str(x[i]) + '_' + str(y[i]) + '_'+ str(w[i]) + '_' + str(h[i]) + ';'        
    writer.writerow([img_name, coordinate[:-1]])
    yolo.predict_clear()

    remain -= 1
    if remain % 100 == 0:
        print(('Remain: %d  \t Time Taken: %.2f min' % (remain, (time.time() - start_time) / 60.0)))
     

csvfile.close()
yolo.close_session()

