#!/usr/bin/env python
# coding: utf-8

# In[5]:

import sys

UNITS = sys.argv[1]
ACTIVATION = sys.argv[2]

import pandas as pd
import numpy as np
import os

# In[80]:

import pickle
file = open("TS.data",'rb')
TS = pickle.load(file)

from keras.layers import RepeatVector
from keras.layers import TimeDistributed
from keras import layers
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras
from keras import layers
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

from keras import backend as K

# In[81]:
# def step1(x):
#     return (1/(1+K.exp(-7*x)) + 1/(1+K.exp(-7*(x+1))) + 1/(1+K.exp(-7*(x-1))))/3
# def step2(x):
#     return (1/(1+K.exp(-7*x)) + 1/(1+K.exp(-7*(x+1))))/2
# def step3(x):
#     return 1/(1+K.exp(-7*x))

model = Sequential()
model.add(Dense(int(UNITS), activation=ACTIVATION,input_shape=(288,)))
# ~ model.add(Dense(int(UNITS), activation=ACTIVATION))
# model.add(Dense(int(UNITS)))

# if ACTIVATION=='step1':
#     model.add(layers.Lambda(step1))
# if ACTIVATION=='step2':
#     model.add(layers.Lambda(step2))
# if ACTIVATION=='step3':
#     model.add(layers.Lambda(step3))
    
model.add(Dense(288,activation='sigmoid')) #since input/output is normalized
model.compile(optimizer='adam', loss='mse')

print(model.summary())



model.fit(TS,TS,epochs=15)


from keras import Model
encoder = Model(model.input, model.layers[-2].output)
print(encoder.summary())

decoder = Model(model.layers[-3].input, model.output)
print(decoder.summary())


encoder.save(UNITS+'-'+ACTIVATION)


# In[92]:


#m = keras.models.load_model("10")

