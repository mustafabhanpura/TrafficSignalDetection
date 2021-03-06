import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from PIL import Image
import os
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential,Model
from keras.layers import Conv2D,MaxPool2D,Dense,Flatten,Dropout

data = []
labels = []
classes = 43
cur_path = os.getcwd()

for i in range(classes):
    path = os.path.join(cur_path,'Train',str(i))
    images = os.listdir(path)
    for a in images:
        try:
            image = Image.open(path + '\\'+ a)
            image = image.resize((30,30))
            image = np.array(image)
            #sim = Image.fromarray(image)
            data.append(image)
            labels.append(i)
        except:
            print("Error loading image")
#Converting lists into numpy arrays
data = np.array(data)
labels = np.array(labels)
a=data
b = labels

print(a.shape,b.shape)
X_train, X_test, y_train,y_test = train_test_split(data,labels,test_size = 0.2,random_state=42)
y_train = to_categorical(y_train,43)
y_test = to_categorical(y_test,43)