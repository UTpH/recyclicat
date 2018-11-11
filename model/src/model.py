import torch
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import torch.nn.functional as F

nclasses = 2 # reclable and non-recyclable
IMG_SIZE = 32

class Net(nn.Module):    
<<<<<<< HEAD
        def __init__(self):
           super(Net, self).__init__()
           self.conv1 = nn.Conv2d(3, 150, kernel_size=5, padding=0)
           self.conv2 = nn.Conv2d(150, 200, kernel_size=3, padding=0)
           self.conv3 = nn.Conv2d(200, 300, kernel_size=3, padding=0)
           self.fc1 = nn.Linear(1200, 50)
           self.conv2_drop = nn.Dropout2d()
           self.fc2 = nn.Linear(50, nclasses)


        def forward(self, x):
              x = F.relu(F.max_pool2d(self.conv1(x), 2))
              x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
              x = F.relu(F.max_pool2d(self.conv2_drop(self.conv3(x)), 2))
              x = x.view(-1, 1200)
              x = F.relu(self.fc1(x))
              x = F.dropout(x, training=self.training)
              x = self.fc2(x)
              return F.log_softmax(x)
=======
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 150, kernel_size=5, padding=0)
        self.conv2 = nn.Conv2d(150, 200, kernel_size=3, padding=0)
        self.conv3 = nn.Conv2d(200, 300, kernel_size=3, padding=0)
        self.fc1 = nn.Linear(1200, 50)
        self.conv2_drop = nn.Dropout2d()
        self.fc2 = nn.Linear(50, nclasses)


    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv3(x)), 2))
        x = x.view(-1, 1200)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x)
>>>>>>> 144d4774e06668620d722e1c9b8bdf665dffc8dd
