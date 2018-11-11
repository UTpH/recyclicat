import os 
import constants
import numpy as np
from scipy import misc, ndimage

def resize(image,dim1, dim2):
    return misc.imresize(image, (dim1, dim2))

def fileWalk(directory, destPath):
    try:
        os.makedirs(destPath)
            
    except OSError:
        if not os.path.isdir(destPath):
            raise

    for subdir, dirs, files in os.walk(directory):
        for fi in files:
            if len(fi) <=4 or fi[-4:] != '.jpg':
                continue
            try:
                pic = misc.imread(os.path.join(subdir,fi))
                dim1 =len(pic)
                dim2 = len(pic[0])
                if dim1 > dim2:
                    pic = np.rot90(pic)

                    picResized = resize(pic,constants.DIM1, 
                            constants.DIM2)
                    misc.imsave(os.path.join(destPath,fi),picResized)
            except:
                continue

def main():
    """
    our directory structure is --
    
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
    
    """
    folders = []
    data_folder = os.chdir('../data/dataset-resized/')
    print(os.getcwd())
    for folder in os.listdir(data_folder):
        if folder.endswith("_nr"):
            folders.append(folder)
    
    destp = os.path.join(os.getcwd(), 'ur_resized')
    for f in folders:
        fileWalk(f, os.path.join(destp,str(f)))


if __name__ == '__main__':
        main()
