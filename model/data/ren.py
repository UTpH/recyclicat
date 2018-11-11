import os
import numpy as np
import pandas as pd

data_ren = pd.read_csv('num_labelled_data.csv')
files=  os.chdir('numb_data/')
count = 0
"""
for f in os.listdir(files):
   #print(f)
   ind = ( data_ren.loc[data_ren['image']==f[:-4]].index[0])
   os.rename(f, str(count)+'.jpg')
   #f = str(count)+ '.jpg'
   data_ren.loc[ind,'image'] = count
   count+=1
del data_ren['Unnamed: 0']
"""
del data_ren['Unnamed: 0']
print(data_ren.head())
data_ren.to_csv('num_labelled_data.csv',index=False)
   
