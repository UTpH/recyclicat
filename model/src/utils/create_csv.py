import pandas as pd
import numpy as np
import os


lst = []
data = os.chdir('../data/dataset-resized/')
for fol in os.listdir(data):
    if os.path.isdir(fol):
        label = fol[-1:]
        for img in os.listdir(fol): 
            if img.endswith('.jpg'):
                #print([img[:-4], label])
                #data_csv = data_csv.append([img[:-4], label]) 
                lst.append([img[:-4], label])

data_csv = pd.DataFrame(lst, columns = ['image','label'])
print(data_csv.head())    
data_csv.to_csv('labelled_data.csv')
