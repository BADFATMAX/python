import torch
import torchvision
from torchvision.transforms import ToTensor
import torchvision.models as models
from torchvision import transforms
import cv2
import numpy as np
from matplotlib import pyplot as plt
import PIL
from torch.autograd import Variable
import torch.nn as nn
#torch.cuda.is_available()
# model = torch.hub.load('pytorch/vision:v0.10.0', 'mobilenet_v2', pretrained=False)
model = models.mobilenet_v2(num_classes=10)
model.train()

training_data = torchvision.datasets.FashionMNIST(root="dataset/",
                                                  train=True,
                                                  download=True,
                                                  transform=ToTensor())

data_loader = torch.utils.data.DataLoader(training_data,
                                          batch_size=32,
                                          shuffle=True)

def preprocc(input):
    output = []
    for im in input:
        image = cv2.cvtColor(np.array(im[0]), cv2.COLOR_GRAY2RGB)
        output.append(image)
    output = torch.Tensor(output).permute(0, 3, 1, 2)
    return output

opt = torch.optim.SGD(model.parameters(), lr=0.1)

l1_loss = nn.CrossEntropyLoss()
l1_loss.requres_grad = True

for epoch in range(10):
    sum = 0
    i = 0
    for x, y in data_loader:
        opt.zero_grad()
        x = preprocc(x)
        x.requires_grad_()

        y_pred = model(x)
        # y_pred = torch.argmax(y_pred, dim=1)

        # y = y * 1.0
        # y_pred = y_pred * 1.0

        y_pred.requires_grad_()

        loss = l1_loss(y_pred, y)
        loss.backward()
        print(i)
        sum += loss
        print('Loss', loss.item())
        opt.step()
        i += 1
    print(sum / 1875)
