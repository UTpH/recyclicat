from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
import errno
import contextlib

# Training settings
parser = argparse.ArgumentParser(description='Trash- Recyclica')
parser.add_argument('--data', type=str, default='../data/numb_data', metavar='D',
                            help="folder where data is located. train_data.zip and test_data.zip need to be found in the folder")
parser.add_argument('--csv', type=str, default='../data/num_labelled_data.csv', metavar='C',
                            help="CSV's location")
parser.add_argument('--batch-size', type=int, default=64, metavar='N',
                            help='input batch size for training (default: 64)')
parser.add_argument('--epochs', type=int, default=10, metavar='N',
                            help='number of epochs to train (default: 10)')
parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
                            help='learning rate (default: 0.01)')
parser.add_argument('--momentum', type=float, default=0.5, metavar='M',
                            help='SGD momentum (default: 0.5)')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                            help='random seed (default: 1)')
parser.add_argument('--log-interval', type=int, default=10, metavar='N',
                            help='how many batches to wait before logging training status')
args = parser.parse_args()

torch.manual_seed(args.seed)

from dataloader import TrashData, ToTensor 

data_used = TrashData(args.data,args.csv,transform=ToTensor())

 # for i in range(len(data_used)):
 #         sample = data_used[i]
 #         print(i, sample['image'],sample['label'])
 #         if i == 3:
 #              break
train_ =[]
for i in range(int(0.8*len(data_used))):
    j = data_used[i]
    train_.append(j)
val_ =[]
for k in range( int(0.8*len(data_used)), len(data_used)):
    l = data_used[k]
    val_.append(l)

print(len(train_))
print(len(val_))
train_loader = torch.utils.data.DataLoader(train_, batch_size =64, shuffle =True,
            num_workers =1)

val_loader = torch.utils.data.DataLoader(val_, batch_size = 64, shuffle = False,
               num_workers = 1)

    


 



"""Below this is probably the same thing"""
from model import Net
model = Net()
optimizer = optim.SGD(model.parameters(), lr=args.lr, momentum=args.momentum)


def train(epoch):
    model.train()
    for batch_idx, (data, target) in (train_loader):
        print(batch_idx, data,target)
        data, target = Variable(data), Variable(target)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % args.log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                        100. * batch_idx / len(train_loader), loss.data[0]))


def validation():
        model.eval()
        validation_loss = 0
        correct = 0
        for data, target in val_loader:
            data, target = Variable(data, volatile=True), Variable(target)
            output = model(data)
            validation_loss += F.nll_loss(output, target, size_average=False).data[0] # sum up batch loss
            pred = output.data.max(1, keepdim=True)[1] # get the index of the max log-probability
            correct += pred.eq(target.data.view_as(pred)).cpu().sum()

        validation_loss /= len(val_loader.dataset)
        print('\nValidation set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(validation_loss, correct, len(val_loader.dataset),
            100. * correct / len(val_loader.dataset)))

for epoch in range(1, args.epochs + 1):
        train(epoch)
        validation()
        model_file = 'model_' + str(epoch) + '.pth'
        torch.save(model.state_dict(), model_file)
