# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 19:50:43 2018

@author: pH
"""

import sys
import os
import torch
import argparse
from tqdm import tqdm
from model import Net
import PIL.Image as Image
from data import data_transforms
from torch.autograd import Variable

parser = argparse.ArgumentParser(description='PyTorch Recyclicat test')
parser.add_argument('--model', type=str, metavar='M',
                    help="the model file to be evaluated. Usually it is of the form model_X.pth")
parser.add_argument('--infile', type=str, default='x.jpg', metavar='D',
                    help="name of the input image")

args = parser.parse_args()
state_dict = torch.load(args.model)
model = Net()
model.load_state_dict(state_dict)
model.eval()

def pil_loader(path):
    # open path as file to avoid ResourceWarning (https://github.com/python-pillow/Pillow/issues/835)
    with open(path, 'rb') as f:
        with Image.open(f) as img:
            return img.convert('RGB')


for f in tqdm(os.listdir(test_dir)):
    if 'ppm' in f:
        data = data_transforms(pil_loader('/' + f))
        data = data.view(1, data.size(0), data.size(1), data.size(2))
        data = Variable(data, volatile=True)
        output = model(data)
        pred = output.data.max(1, keepdim=True)[1]

        file_id = f[0:5]
        output_file.write("%s,%d\n" % (file_id, pred))

if(pred == 0):
    classification = 'Non - Recyclable'
else:
    classification = 'Recyclable'
print(classification)
        





if __name__ == '__main__':
    print("Got through ", sys.argv[1])
