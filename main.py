import os
from skimage.io import imread
from skimage.transform import resize
import numpy as np

input_dir = 'data'
categories = ['empty','not_empty']

data= []
labels= []

for category_idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir,category)):
        img_path = os.path.join(input_dir,category,file)
        img= imread(img_path)
        img = resize(img,(15,15))
        data.append(img.flatted())
        labels.append(category_idx)
        