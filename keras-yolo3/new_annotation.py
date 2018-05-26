import pandas as pd
from math import isnan

annotation_dir = '/media/zyzhong/Data/data3/HualuCUP/'

train = pd.read_csv(annotation_dir + 'train_1w.csv')
list_file = open(annotation_dir + 'annotation.txt', 'w')
img_list = list(set(list(train.name)))
number = len(img_list)
for i in range(number):
    list_file.write(train.name[i])
    if str(train.coordinate[i]).endswith(';'):  
        coordinates = str(train.coordinate[i])[:-1].split(';')
    else:
        coordinates = str(train.coordinate[i]).split(';')
    
    for coordinate in coordinates:
        list_file.write(' ')
        coords = str(coordinate).split('_')
        for coord in coords:
            coord = float(coord)
            if isnan(coord):
                print(i)
                list_file.write('\n')
        
        coords[2] = int(float(coords[0]) + float(coords[2]))
        coords[3] = int(float(coords[1]) + float(coords[3])) 
      
        for coord in coords:
            coord = str(coord)
            print(coord)
            list_file.write(coord + ',')
        list_file.write('0')
    list_file.write('\n')
list_file.close()
