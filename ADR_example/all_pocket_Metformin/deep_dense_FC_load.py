import pandas as pd
import tensorflow as tf

import keras
#import keras.backend as K

from keras.models import Model, load_model
from keras.layers import Input, merge, Activation, Dropout, Dense, concatenate, Concatenate, Flatten
from keras.layers.convolutional import Convolution1D
from keras.layers.pooling import AveragePooling1D, GlobalAveragePooling1D, MaxPool1D
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2

from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator

#import xgboost as xgb
from sklearn import metrics

import os
import yaml
import numpy as np

#import h5py
#with h5py.File('pos_aa1000.h5', 'r') as hf:
#    pos_samples = hf['name-of-dataset1'][:]
#with h5py.File('neg_aa1000.h5', 'r') as hf:
#    neg_samples = hf['name-of-dataset2'][:]

pos = np.array(pd.read_hdf('mp_data/pos.h5', 'df'), dtype=float)

#pos=pos.astpye(float)
#neg=neg.astpye(float)

pos_label = np.ones(pos.shape[0])
test_X = pos


test_X_conv = test_X.reshape((test_X.shape[0], 600, 1))



def preprocess_data(data_set):
    mean = np.mean(data_set)
    std = np.std(data_set)
    
    t = data_set

    t -= mean
    t /= std
    return t

def aucJ(true_labels, predictions):
    
    fpr, tpr, thresholds = metrics.roc_curve(true_labels, predictions, pos_label=1)
    auc = metrics.auc(fpr,tpr)

    return auc

def acc(true, pred):
    
    return np.sum(true == pred) * 1.0 / len(true)

def assess(model, X, label, thre = 0.5):
    
    threshold = thre
    
    pred = model.predict(X)
    pred = pred.flatten()
    
    pred[pred > threshold] = 1
    pred[pred <= threshold] = 0
    
    auc = aucJ(label, pred)
    accuracy = acc(label, pred)
    
    print('auc: ', auc)
    print('accuracy: ', accuracy)




test_X = preprocess_data(test_X)





##model2.fit(x = train_X, y = train_Y, epochs = 15000, batch_size = 8192)

#assess(model2, train_X, train_Y)
#assess(model2, valid_X, valid_Y)
#assess(model2, test_X, test_Y)

##model2.save('FCdenset.h5')

model2 = load_model('FCdense.h5')

#assess(model2, test_X, test_Y)

pred = model2.predict(test_X)
pred = pred.flatten()

import pandas as pd
df=pd.read_csv('mp_data/pos_list.csv', header=None)

name=df.iloc[1:,0].values
listA=zip(list(name),list(pred))
#for i in range(len(pred)):
#     listA[i][0]=pred[i]
#     listA[i][1]=name[i]
y=sorted(listA,key=lambda l:l[1],reverse=True)
fw=open('sorted_out.txt','w')
for i in range(len(y)):
     print (y[i][0], y[i][1])
     fw.write(str(y[i][0]) +"  "+ str(y[i][1]))
     fw.write('\n')



