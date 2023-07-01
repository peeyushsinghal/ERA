import torch.nn as nn
import torch.nn.functional as F # for forward method


class Network(nn.Module):
  def __init__(self, norm = 'bn'):
    super(Network,self).__init__() # extending super class method
    
    drop_out_value = 0.1
    self.norm = norm

    # Input Block
    self.convblock1 = nn.Sequential(
        nn.Conv2d(1,18,3 , bias= False ), # In- 1x28x28, Out- 16x26x26, RF- 3x3, Jump_in -1, Jump_out -1
        nn.ReLU()
        # ,
        # nn.BatchNorm2d(18), # affine=False),
        # nn.Dropout(drop_out_value)
    ) 
    
    if self.norm == 'bn': self.normlayer1 = nn.BatchNorm2d(18)
    if self.norm == 'ln': self.normlayer1 = nn.LayerNorm([18,26,26]) 
    if self.norm == 'gn' : self.normlayer1 = nn.GroupNorm(2,18) # 2 groups of 9 channels each
    self.dropout1 = nn.Dropout(drop_out_value)

    # Conv Block 2
    self.convblock2 = nn.Sequential(
        nn.Conv2d(18,16,3, bias= False ), # In- 16x26x26, Out- 16x24x24, RF- 5x5, Jump_in -1, Jump_out -1
        nn.ReLU()
        # ,
        # nn.BatchNorm2d(16),# affine=False),
        # nn.Dropout(drop_out_value)
    ) 

    if self.norm == 'bn': self.normlayer2 = nn.BatchNorm2d(16)
    if self.norm == 'ln': self.normlayer2 = nn.LayerNorm([16,24,24]) 
    if self.norm == 'gn' : self.normlayer2 = nn.GroupNorm(2,16) # 2 groups of 8 channels each
    self.dropout2 = nn.Dropout(drop_out_value)


    # Conv Block 3
    self.convblock3 = nn.Sequential(
        nn.Conv2d(16,16,3, bias= False ), # In- 16x24x24, Out- 16x22x22, RF- 7x7, Jump_in -1, Jump_out -1
        nn.ReLU()
        # ,
        # nn.BatchNorm2d(16),# affine=False),
        # nn.Dropout(drop_out_value)
    ) 

    if self.norm == 'bn': self.normlayer3 = nn.BatchNorm2d(16)
    if self.norm == 'ln': self.normlayer3 = nn.LayerNorm([16,22,22]) 
    if self.norm == 'gn' : self.normlayer3 = nn.GroupNorm(2,16) # 2 groups of 8 channels each
    self.dropout3 = nn.Dropout(drop_out_value)

    # Transition Block 1 (this also includes a conv block)
    self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2) # In- 16x22x22, Out- 16x11x11, RF- 8x8, Jump_in -1, Jump_out -2
    # self.convblock4 = nn.Sequential(
    #     nn.Conv2d(32,16,1), # In- 32x12x12, Out- 16x12x12, RF- 8x8, Jump_in -2, Jump_out -2
    #     nn.ReLU(),
    #     nn.BatchNorm2d(16),
    #     nn.Dropout(drop_out_value)
    # ) 

    # Conv Block 5
    self.convblock5 = nn.Sequential(
        nn.Conv2d(16,16,3, bias= False ), # In- 16x11x11, Out- 16x9x9, RF- 12x12, Jump_in -2, Jump_out -2
        nn.ReLU()
        # ,
        # nn.BatchNorm2d(16),# affine=False),
        # nn.Dropout(drop_out_value)
    ) 

    if self.norm == 'bn': self.normlayer5 = nn.BatchNorm2d(16)
    if self.norm == 'ln': self.normlayer5 = nn.LayerNorm([16,9,9]) 
    if self.norm == 'gn' : self.normlayer5 = nn.GroupNorm(2,16) # 2 groups of 8 channels each
    self.dropout5 = nn.Dropout(drop_out_value)

    # Conv Block 6
    self.convblock6 = nn.Sequential(
        nn.Conv2d(16,16,3, bias= False ), # In- 16x9x9, Out- 16x7x7, RF- 16x16, Jump_in -2, Jump_out -2
        nn.ReLU()
        # ,
        # nn.BatchNorm2d(16),# affine=False),
        # nn.Dropout(drop_out_value)
    ) 

    if self.norm == 'bn': self.normlayer6 = nn.BatchNorm2d(16)
    if self.norm == 'ln': self.normlayer6 = nn.LayerNorm([16,7,7]) 
    if self.norm == 'gn' : self.normlayer6 = nn.GroupNorm(2,16) # 2 groups of 8 channels each
    self.dropout6 = nn.Dropout(drop_out_value)

    # Output Block
    self.convblock7 = nn.Sequential(
        nn.Conv2d(16,10,1, bias= False ), # In- 16x7x7, Out- 10x7x7, RF- 16x16, Jump_in -2, Jump_out -2
        # nn.ReLU()
        # ,
        # nn.BatchNorm2d(10, affine=True),
        # nn.Dropout(drop_out_value)
    ) 

    self.gap = nn.AvgPool2d(7) # In- 10x7x7, Out- 10x1x1, RF- 16x16, Jump_in -2, Jump_out -2


  def forward(self,x):

    x = self.convblock1(x)
    x = self.dropout1(self.normlayer1(x))
    x = self.convblock2(x)
    x = self.dropout2(self.normlayer2(x))
    x = self.convblock3(x)
    x = self.dropout3(self.normlayer3(x))

    x = self.pool1(x)
    # x = self.convblock4(x)
    x = self.convblock5(x)
    x = self.dropout5(self.normlayer5(x))
    x = self.convblock6(x)
    x = self.dropout6(self.normlayer6(x))

    x = self.convblock7(x)

    x = self.gap(x)

    # Flattening
    x = x.view(-1,10)
    return F.log_softmax(x,dim=-1)

