#!/usr/bin/env python
# coding: utf-8

# In[5]:

import sys


DIR='PM0'
import pandas as pd
import numpy as np
import os
FILES=[]
for F in os.listdir('./{}/'.format(DIR)):
    if '.csv' in F:
        if 'A-' in F:
            FILES.append('./{}/'.format(DIR)+F)

DIR='PM1'
for F in os.listdir('./{}/'.format(DIR)):
    if '.csv' in F:
        if 'A-' in F:
            FILES.append('./{}/'.format(DIR)+F)


DIR='PM7'
for F in os.listdir('./{}/'.format(DIR)):
    if '.csv' in F:
        if 'A-' in F:
            FILES.append('./{}/'.format(DIR)+F)

print(len(FILES))

def getS(F):
    dt = pd.read_csv(F,sep='\t')
    
    S=None
    
#     print(dt.columns)
    
    if 'Lane 2 Speed (mph)' in dt.columns:
        
        S = (dt['Lane 1 Speed (mph)']+dt['Lane 2 Speed (mph)'])/2
        return S
        
    if 'Lane 1 Speed (mph)' in dt.columns:
        
        S = dt['Lane 1 Speed (mph)']
        return S


def getF(F):
    dt = pd.read_csv(F,sep='\t')
    
    S=None

    if 'Lane 2 Flow (Veh/5 Minutes)' in dt.columns:
        
        S = (dt['Lane 1 Flow (Veh/5 Minutes)']+dt['Lane 2 Flow (Veh/5 Minutes)'])/2
        return S
            
    if 'Lane 1 Flow (Veh/5 Minutes)' in dt.columns:
        
        S = dt['Lane 1 Flow (Veh/5 Minutes)']
        return S

    return S

FLOWS=[]
for F in FILES:
    S = getF(F)
    if S is not None and len(S)==288:
        FLOWS.append(S.values)

SPEEDS=[]
for F in FILES:
    S = getS(F)
    if S is not None and len(S)==288:
        SPEEDS.append(S.values)

SPEEDS = np.array(SPEEDS)
FLOWS = np.array(FLOWS)

import matplotlib.pyplot as plt

print('SPEEDS.max()',SPEEDS.max()) #85.25
SPEEDS = SPEEDS/SPEEDS.max()

print('FLOWS.max()',FLOWS.max()) #224.5
FLOWS = FLOWS/FLOWS.max()


TS = np.concatenate([SPEEDS,FLOWS],axis=0)
print(TS.shape)

import pickle
filehandler = open(b"TS.data","wb")
pickle.dump(TS,filehandler)
