import torch
import torch.nn as nn
import torch.nn.functional as F
from torchsummary import summary
from tqdm import tqdm


class Net(nn.Module):
    #This defines the structure of the NN.
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, bias = False) # 26x26 , rin :1, rout:3, jin :1, jout : 1
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, bias = False) # 24 x 24 rin :3, rout:5, jin :1, jout : 1
        # max pool - 12x12x64 rin : 5, rout:6, jin :1, jout : 2
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, bias = False) # 10x10 rin : 6, rout:10, jin :2, jout : 2
        self.conv4 = nn.Conv2d(128, 256, kernel_size=3, bias = False) # 8x8 rin : 10, rout:14, jin :2, jout : 2
        # max pool - 4 x 4 x 256 = 4096 rin : 14, rout:16, jin :2, jout : 4
        # self.fc1 = nn.Linear(320, 50)
        self.fc1 = nn.Linear (4096, 50, bias = False)
        self.fc2 = nn.Linear(50, 10, bias = False)

    # def forward(self, x):
    #     x = F.relu(self.conv1(x), 2)
    #     x = F.relu(F.max_pool2d(self.conv2(x), 2)) 
    #     x = F.relu(self.conv3(x), 2)
    #     x = F.relu(F.max_pool2d(self.conv4(x), 2)) 
    #     x = x.view(-1, 320)
    #     x = F.relu(self.fc1(x))
    #     x = self.fc2(x)
    #     return F.log_softmax(x, dim=1)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(F.relu(self.conv2(x)),2,2) 
        x = F.relu(self.conv3(x))
        x = F.max_pool2d(F.relu(self.conv4(x)), 2,2) 
        x = x.view(-1, 4096)#320)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

def print_summary(model):
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    model = model.to(device)
    summary(model, input_size=(1, 28, 28))


train_losses = []
test_losses = []
train_acc = []
test_acc = []

def GetCorrectPredCount(pPrediction, pLabels):
  return pPrediction.argmax(dim=1).eq(pLabels).sum().item()

def model_train(model, device, train_loader, optimizer,train_acc=train_acc,train_losses=train_losses):
  model.train()
  pbar = tqdm(train_loader)

  train_loss = 0
  correct = 0
  processed = 0

  for batch_idx, (data, target) in enumerate(pbar):
    data, target = data.to(device), target.to(device)
    optimizer.zero_grad()

    # Predict
    pred = model(data)

    # Calculate loss
    loss = F.nll_loss(pred, target)
    train_loss+=loss.item()

    # Backpropagation
    loss.backward()
    optimizer.step()
    
    correct += GetCorrectPredCount(pred, target)
    processed += len(data)

    pbar.set_description(desc= f'Train: Loss={loss.item():0.4f} Batch_id={batch_idx} Accuracy={100*correct/processed:0.2f}')

  train_acc.append(100*correct/processed)
  train_losses.append(train_loss/len(train_loader))

def model_test(model, device, test_loader,test_acc=test_acc,test_losses=test_losses):
    model.eval()

    test_loss = 0
    correct = 0

    with torch.no_grad():
        for batch_idx, (data, target) in enumerate(test_loader):
            data, target = data.to(device), target.to(device)

            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item()  # sum up batch loss

            correct += GetCorrectPredCount(output, target)


    test_loss /= len(test_loader.dataset)
    test_acc.append(100. * correct / len(test_loader.dataset))
    test_losses.append(test_loss)

    print('Test set: Average loss: {:.4f}, Accuracy: {}/{} ({:.2f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))
     