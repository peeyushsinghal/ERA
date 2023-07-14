# Assignment
1. Write a custom ResNet architecture for CIFAR10 that has the following architecture:
  - PrepLayer - Conv 3x3 s1, p1) >> BN >> RELU `[out channels = 64]`
  - Layer1
    - X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU `[out channels = 128]`
    - R1 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) `[out channels = 128]` 
    - Add(X, R1)
  - Layer 2
    - Conv 3x3 `[out channels = 256]`
    - MaxPooling2D
    - BN
    - ReLU
  - Layer 3
    - X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU `[out channels = 512]`
    - R2 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) `[out channels = 512]`
    - Add(X, R2)
  - Max Pooling with Kernel Size 4
  - FC Layer 
  - SoftMax
2. Uses One Cycle Policy such that:
  - Total Epochs = 24
  - Max at Epoch = 5
  - LRMIN = FIND
  - LRMAX = FIND
  - No Annihilation
3. Uses these transforms
  - RandomCrop(32, 32) (after padding of 4)
  - FlipLR
  - Followed by CutOut(8, 8)
4. Batch size = 512
5. Target Accuracy: 90%
6. Use ADAM, and CrossEntropyLoss
---
## Transformation
![image](https://github.com/peeyushsinghal/ERA/assets/10797988/1c51fac3-f96a-4756-86d1-0d47aa7fda6b)
----
## Model
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 64, 32, 32]           1,792
       BatchNorm2d-2           [-1, 64, 32, 32]             128
              ReLU-3           [-1, 64, 32, 32]               0
            Conv2d-4          [-1, 128, 32, 32]          73,856
         MaxPool2d-5          [-1, 128, 16, 16]               0
       BatchNorm2d-6          [-1, 128, 16, 16]             256
              ReLU-7          [-1, 128, 16, 16]               0
        LayerBlock-8          [-1, 128, 16, 16]               0
            Conv2d-9          [-1, 128, 16, 16]         147,584
      BatchNorm2d-10          [-1, 128, 16, 16]             256
             ReLU-11          [-1, 128, 16, 16]               0
           Conv2d-12          [-1, 128, 16, 16]         147,584
      BatchNorm2d-13          [-1, 128, 16, 16]             256
             ReLU-14          [-1, 128, 16, 16]               0
         ResBlock-15          [-1, 128, 16, 16]               0
           Conv2d-16          [-1, 256, 16, 16]         295,168
        MaxPool2d-17            [-1, 256, 8, 8]               0
      BatchNorm2d-18            [-1, 256, 8, 8]             512
             ReLU-19            [-1, 256, 8, 8]               0
       LayerBlock-20            [-1, 256, 8, 8]               0
           Conv2d-21            [-1, 256, 8, 8]         590,080
      BatchNorm2d-22            [-1, 256, 8, 8]             512
             ReLU-23            [-1, 256, 8, 8]               0
           Conv2d-24            [-1, 256, 8, 8]         590,080
      BatchNorm2d-25            [-1, 256, 8, 8]             512
             ReLU-26            [-1, 256, 8, 8]               0
         ResBlock-27            [-1, 256, 8, 8]               0
           Conv2d-28            [-1, 512, 8, 8]       1,180,160
        MaxPool2d-29            [-1, 512, 4, 4]               0
      BatchNorm2d-30            [-1, 512, 4, 4]           1,024
             ReLU-31            [-1, 512, 4, 4]               0
       LayerBlock-32            [-1, 512, 4, 4]               0
           Conv2d-33            [-1, 512, 4, 4]       2,359,808
      BatchNorm2d-34            [-1, 512, 4, 4]           1,024
             ReLU-35            [-1, 512, 4, 4]               0
           Conv2d-36            [-1, 512, 4, 4]       2,359,808
      BatchNorm2d-37            [-1, 512, 4, 4]           1,024
             ReLU-38            [-1, 512, 4, 4]               0
         ResBlock-39            [-1, 512, 4, 4]               0
        MaxPool2d-40            [-1, 512, 1, 1]               0
           Linear-41                   [-1, 10]           5,130
================================================================
Total params: 7,756,554
Trainable params: 7,756,554
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.01
Forward/backward pass size (MB): 8.07
Params size (MB): 29.59
Estimated Total Size (MB): 37.67
----------------------------------------------------------------
## Training
EPOCH: 1
  0%|          | 0/98 [00:00<?, ?it/s]/usr/local/lib/python3.10/dist-packages/torch/utils/data/dataloader.py:560: UserWarning: This DataLoader will create 4 worker processes in total. Our suggested max number of worker in current system is 2, which is smaller than what this DataLoader is going to create. Please be aware that excessive worker creation might get DataLoader running slow or even freeze, lower the worker number to avoid potential slowness/freeze if necessary.
  warnings.warn(_create_warning_msg(
Loss=1.438926339149475 Batch_id=97 Accuracy=34.96: 100%|██████████| 98/98 [00:24<00:00,  3.98it/s]
Test set: Average loss: 0.0001, Accuracy: 4995/10000 (49.95%)

EPOCH: 2
Loss=1.057191252708435 Batch_id=97 Accuracy=55.33: 100%|██████████| 98/98 [00:24<00:00,  3.99it/s]
Test set: Average loss: 0.0002, Accuracy: 5449/10000 (54.49%)

EPOCH: 3
Loss=0.8681988716125488 Batch_id=97 Accuracy=66.40: 100%|██████████| 98/98 [00:26<00:00,  3.72it/s]
Test set: Average loss: 0.0001, Accuracy: 6649/10000 (66.49%)

EPOCH: 4
Loss=0.7527937293052673 Batch_id=97 Accuracy=74.59: 100%|██████████| 98/98 [00:27<00:00,  3.59it/s]
Test set: Average loss: 0.0001, Accuracy: 7098/10000 (70.98%)

EPOCH: 5
Loss=0.6469466090202332 Batch_id=97 Accuracy=78.71: 100%|██████████| 98/98 [00:25<00:00,  3.85it/s]
Test set: Average loss: 0.0001, Accuracy: 7887/10000 (78.87%)

EPOCH: 6
Loss=0.4306267201900482 Batch_id=97 Accuracy=82.31: 100%|██████████| 98/98 [00:26<00:00,  3.72it/s]
Test set: Average loss: 0.0001, Accuracy: 7997/10000 (79.97%)

EPOCH: 7
Loss=0.3398405909538269 Batch_id=97 Accuracy=85.38: 100%|██████████| 98/98 [00:25<00:00,  3.79it/s]
Test set: Average loss: 0.0000, Accuracy: 8277/10000 (82.77%)

EPOCH: 8
Loss=0.3425373435020447 Batch_id=97 Accuracy=87.06: 100%|██████████| 98/98 [00:28<00:00,  3.43it/s]
Test set: Average loss: 0.0000, Accuracy: 8476/10000 (84.76%)

EPOCH: 9
Loss=0.3593102693557739 Batch_id=97 Accuracy=89.37: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]
Test set: Average loss: 0.0000, Accuracy: 8384/10000 (83.84%)

EPOCH: 10
Loss=0.33744436502456665 Batch_id=97 Accuracy=90.30: 100%|██████████| 98/98 [00:24<00:00,  4.05it/s]
Test set: Average loss: 0.0000, Accuracy: 8582/10000 (85.82%)

EPOCH: 11
Loss=0.2301202267408371 Batch_id=97 Accuracy=92.09: 100%|██████████| 98/98 [00:24<00:00,  4.04it/s]
Test set: Average loss: 0.0000, Accuracy: 8760/10000 (87.60%)

EPOCH: 12
Loss=0.22093932330608368 Batch_id=97 Accuracy=93.02: 100%|██████████| 98/98 [00:24<00:00,  4.04it/s]
Test set: Average loss: 0.0001, Accuracy: 8526/10000 (85.26%)

EPOCH: 13
Loss=0.1260785311460495 Batch_id=97 Accuracy=94.05: 100%|██████████| 98/98 [00:24<00:00,  4.04it/s]
Test set: Average loss: 0.0000, Accuracy: 8676/10000 (86.76%)

EPOCH: 14
Loss=0.13487374782562256 Batch_id=97 Accuracy=95.05: 100%|██████████| 98/98 [00:24<00:00,  4.02it/s]
Test set: Average loss: 0.0000, Accuracy: 8900/10000 (89.00%)

EPOCH: 15
Loss=0.12782709300518036 Batch_id=97 Accuracy=95.94: 100%|██████████| 98/98 [00:24<00:00,  3.96it/s]
Test set: Average loss: 0.0000, Accuracy: 8837/10000 (88.37%)

EPOCH: 16
Loss=0.0989096388220787 Batch_id=97 Accuracy=96.44: 100%|██████████| 98/98 [00:24<00:00,  4.06it/s]
Test set: Average loss: 0.0000, Accuracy: 8996/10000 (89.96%)

EPOCH: 17
Loss=0.05447838827967644 Batch_id=97 Accuracy=97.20: 100%|██████████| 98/98 [00:24<00:00,  4.04it/s]
Test set: Average loss: 0.0000, Accuracy: 9018/10000 (90.18%)

EPOCH: 18
Loss=0.07322374731302261 Batch_id=97 Accuracy=97.63: 100%|██████████| 98/98 [00:24<00:00,  4.04it/s]
Test set: Average loss: 0.0000, Accuracy: 9093/10000 (90.93%)

EPOCH: 19
Loss=0.02914329618215561 Batch_id=97 Accuracy=97.99: 100%|██████████| 98/98 [00:24<00:00,  4.07it/s]
Test set: Average loss: 0.0000, Accuracy: 9060/10000 (90.60%)

EPOCH: 20
Loss=0.04158638417720795 Batch_id=97 Accuracy=98.47: 100%|██████████| 98/98 [00:24<00:00,  4.03it/s]
Test set: Average loss: 0.0000, Accuracy: 9076/10000 (90.76%)

EPOCH: 21
Loss=0.023691503331065178 Batch_id=97 Accuracy=98.71: 100%|██████████| 98/98 [00:24<00:00,  4.05it/s]
Test set: Average loss: 0.0000, Accuracy: 9132/10000 (91.32%)

EPOCH: 22
Loss=0.020311063155531883 Batch_id=97 Accuracy=99.09: 100%|██████████| 98/98 [00:24<00:00,  4.04it/s]
Test set: Average loss: 0.0000, Accuracy: 9162/10000 (91.62%)

EPOCH: 23
Loss=0.011509985662996769 Batch_id=97 Accuracy=99.22: 100%|██████████| 98/98 [00:24<00:00,  4.02it/s]
Test set: Average loss: 0.0000, Accuracy: 9182/10000 (91.82%)

EPOCH: 24
Loss=0.03191109374165535 Batch_id=97 Accuracy=99.33: 100%|██████████| 98/98 [00:24<00:00,  4.05it/s]
Test set: Average loss: 0.0000, Accuracy: 9199/10000 (91.99%)
----
## training output
![image](https://github.com/peeyushsinghal/ERA/assets/10797988/e7171e3c-94a4-480c-8f60-abdf564822c3)

---
## Classification

Accuracy of plane : 87 %
Accuracy of   car : 100 %
Accuracy of  bird : 90 %
Accuracy of   cat : 85 %
Accuracy of  deer : 90 %
Accuracy of   dog : 100 %
Accuracy of  frog : 75 %
Accuracy of horse : 88 %
Accuracy of  ship : 100 %
Accuracy of truck : 90 %

------
## Misclassification
![image](https://github.com/peeyushsinghal/ERA/assets/10797988/180b400e-553f-4dcb-bd14-8bba4fda93c6)

