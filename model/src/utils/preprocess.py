import numpy as np 
from PIL import Image
import os
"""
├── data
│   ├── dataset-resized
│   │   ├── aluminium_nr
│   │   ├── cardboard_r
│   │   ├── ceramic_nr
│   │   ├── clothing-waste
│   │   ├── glass_r
│   │   ├── metal_r
│   │   ├── paper_r
│   │   ├── pizza-boxes_nr
│   │   ├── plastic_r
│   │   ├── soiled-paper-towels_nr
│   │   ├── styrofoam_nr
│   │   ├── trash_r
│   │   ├── unrecyclable
│   │   └── waste-food_nr
│   └── __MACOSX
│       └── dataset-resized
│           └── cardboard
└── src
    └── __pycache__
"""
folder = []
#print(os.getcwd())
image_cats =os.listdir( os.chdir('../data/dataset-resized/'))
for f in image_cats:
    if os.path.isdir(f):
        folder.append(f)

print(folder)
imag_folder = os.getcwd()

for fol in folder:
    count = 0
    count_ppm = 0
    for fi in os.listdir(os.path.join(imag_folder,fol)):
        if fi.endswith('.jpg'):
              count+=1
              fi_new = fi[:-4]
              os.chdir(os.path.join(imag_folder, fol))
              #print(os.getcwd())
              try:
                image= Image.open(fi)
                #image1 = image.resize((200,200)).save(fi_new + '.ppm')
              except OSError:
                continue
        else:
             count_ppm+=1
    print(fol,count)    



