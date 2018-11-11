from __future__ import print_function
import zipfile
import os
import torch 
from skimage import io, transform
import numpy as np
import pandas as pd
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

class TrashData(Dataset):
    """Trash Dataset"""
    def __init__(self, image_fol, csv_file, transform=None):
        self.csv_file = pd.read_csv(csv_file)
        self.image_fol = image_fol
        self.transform = transform

    def __len__(self):
        return len(self.csv_file)

    def __getitem__(self, idx):
             # print(self.image_fol,str(self.csv_file.loc[idx,'image']) + '.jpg')
          # print(idx, type(idx))
         img_name = os.path.join(self.image_fol,str(self.csv_file.at[idx,'image']) + '.jpg')     
         try: 
           #print(str(self.csv_file.loc[idx,'image'].values+ '.jpg')) 
           if img_name is not None:
                #print(img_name)
                image = io.imread(img_name)
                labels = self.csv_file.loc[idx,'label']
                sample = {'image': image, 'label':labels}
                return sample
         except:
            pass 

#data_sample = TrashData(image_fol = '../data/all_data/',csv_file= '../data/labelled_data.csv')
#print(data_sample[1])

class ToTensor(object):
    def __call__(self,sample):
        image, label = sample['image'],sample['label']
        return {'image': torch.from_numpy(image),
                'label': torch.from_numpy(label)}
        

        
