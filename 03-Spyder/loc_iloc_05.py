#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:27:54 2018

@author: usrdel
"""

import pandas as pd
import os

df = pd.read_pickle('/Users/usrdel/Documents/GitHub/eguez-sarzosa-vicente-adrian-python/03-Spyder/data/artwork_data_frame.pickle')

df.loc[1035,'artist']

# df.loc[0,0] # Error

df.iloc[0,1]

df.iloc[0,:]

df.iloc[0:2,0:2]

df['height']
df['width']
#df['height'] * df['width']
df_width = df['width']
dfsort_values = df['width'].sort_values()
dfsort_values_head = df['width'].sort_values().head(100)
dfsort_values_tail = df['width'].sort_values().tail(100)

pd.to_numeric(df['width'])

a = pd.to_numeric(df['width'], errors='coerce')
b = pd.to_numeric(df['height'], errors='coerce')

df.loc[:,'width'] = a
df.iloc[:,6] = b


area = df['height'] * df['width']





























