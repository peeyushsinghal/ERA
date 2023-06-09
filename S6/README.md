S6 Assignment - 2 parts

PART 1
------
Screenshot of excel file
-----------------------

Steps
--------
Loop 1, 2, 3 for n times
1. Forward Pass : Understanding total loss given the current weights
		
- h1=w1 * i1 + w2 * i2			
- h2=w3 * i1 + w4 * i2			
- a_h1 = σ(h1) =1/(1+exp(-h1))			
- a_h2 = σ(h2) =1/(1+exp(-h2))			
- o1 = w5 * a_h1 + w6 * a_h2 			
- o2 = w7 * a_h1 + w8 * a_h2 			
- a_o1 = σ(o1) =1/(1+exp(-o1))			
- a_o2 = σ(o2) =1/(1+exp(-o2))			
- E1 = 0.5* (t1-a_o1)^2			
- E2 = 0.5* (t2-a_o2)^2			
- E_t = E1 + E2			

2. Finding partial derivative of the total loss with respect to weights
- 𝜕E_t/𝜕w1 = [(a_o1-t1) * a_o1*(1-a_o1)*w5+(a_o2-t2) * a_o2*(1-a_o2)*w7]*[a_h1*(1-a_h1)]*[i1]
- 𝜕E_t/𝜕w2 = [(a_o1-t1) * a_o1*(1-a_o1)*w5+(a_o2-t2) * a_o2*(1-a_o2)*w7]*[a_h1*(1-a_h1)]*[i2]
- 𝜕E_t/𝜕w3 = [(a_o1-t1) * a_o1*(1-a_o1)*w6+(a_o2-t2) * a_o2*(1-a_o2)*w8]*[a_h2*(1-a_h2)]*[i1]
- 𝜕E_t/𝜕w4 = [(a_o1-t1) * a_o1*(1-a_o1)*w6+(a_o2-t2) * a_o2*(1-a_o2)*w8]*[a_h2*(1-a_h2)]*[i2]
- 𝜕E_t/𝜕w5 =(a_o1-t1) *a_o1*(1-a_o1)*a_h1
- 𝜕E_t/𝜕w6 =(a_o1-t1) *a_o1*(1-a_o1)*a_h2
- 𝜕E_t/𝜕w7 =(a_o2-t2) *a_o2*(1-a_o2)*a_h1
- 𝜕E_t/𝜕w8 =(a_o2-t2) *a_o2*(1-a_o2)*a_h2

3. Updating the weights 
-       wi = wi - η * (𝜕E_t/𝜕wi) , where i = 1,2,3,4,5,6,7,8


Screenshots of Learning Rate changes
-----------------
Learning Rate = 0.1

Learning Rate = 0.2


Learning Rate = 0.5


Learning Rate = 0.8

Learning Rate = 1.0

Learning Rate = 2.0



PART 2
------
ASK
- Refer to this code: COLABLINK (https://colab.research.google.com/drive/1uJZvJdi5VprOQHROtJIHy0mnY2afjNlx#scrollTo=h_Cx9q2QFgM7)
- WRITE IT AGAIN SUCH THAT IT ACHIEVES
- 99.4% validation accuracy
- Less than 20k Parameters
- You can use anything from above you want. 
- Less than 20 Epochs
- Have used BN, Dropout, a Fully connected layer, have used GAP. 

SOLUTION
- 99.49% achieved in Epoch 19 with Total params: 18,738 (see [https://github.com/peeyushsinghal/EVA8/blob/main/S3-Assignment-Solution/EVA4_Session_2.ipynb](https://github.com/peeyushsinghal/ERA/blob/main/S6/ERA_S6.ipynb))
- Use of Conv layers (with and without padding), 
- use of BN : to make sure that the features available to the next layer is good
- use of strided convolutions as opposed to max pooling : used twice
- use of GAP : instead of FC layers

Model Summary
------------
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
            Conv2d-1           [-1, 32, 26, 26]             832
              ReLU-2           [-1, 32, 26, 26]               0
       BatchNorm2d-3           [-1, 32, 26, 26]              64
           Dropout-4           [-1, 32, 26, 26]               0
            Conv2d-5           [-1, 16, 26, 26]           4,624
              ReLU-6           [-1, 16, 26, 26]               0
       BatchNorm2d-7           [-1, 16, 26, 26]              32
           Dropout-8           [-1, 16, 26, 26]               0
            Conv2d-9           [-1, 16, 13, 13]           2,320
             ReLU-10           [-1, 16, 13, 13]               0
      BatchNorm2d-11           [-1, 16, 13, 13]              32
          Dropout-12           [-1, 16, 13, 13]               0
           Conv2d-13           [-1, 24, 13, 13]           3,480
             ReLU-14           [-1, 24, 13, 13]               0
      BatchNorm2d-15           [-1, 24, 13, 13]              48
          Dropout-16           [-1, 24, 13, 13]               0
           Conv2d-17           [-1, 16, 13, 13]           3,472
             ReLU-18           [-1, 16, 13, 13]               0
      BatchNorm2d-19           [-1, 16, 13, 13]              32
          Dropout-20           [-1, 16, 13, 13]               0
           Conv2d-21             [-1, 16, 7, 7]           2,320
             ReLU-22             [-1, 16, 7, 7]               0
      BatchNorm2d-23             [-1, 16, 7, 7]              32
          Dropout-24             [-1, 16, 7, 7]               0
           Conv2d-25             [-1, 10, 5, 5]           1,450
        AvgPool2d-26             [-1, 10, 1, 1]               0
Total params: 18,738
Trainable params: 18,738
Non-trainable params: 0
Input size (MB): 0.00
Forward/backward pass size (MB): 1.30
Params size (MB): 0.07
Estimated Total Size (MB): 1.38

Training Logs
------------
EPOCH:  1
  0%|          | 0/469 [00:00<?, ?it/s]<ipython-input-26-20cad0239d65>:101: UserWarning: Implicit dimension choice for log_softmax has been deprecated. Change the call to include dim=X as an argument.
  return F.log_softmax(x)
loss=0.06719405204057693 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 24.57it/s]
Test set: Average loss: 0.0673, Accuracy: 9805/10000 (98.05%)

EPOCH:  2
loss=0.05021698772907257 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 24.23it/s]
Test set: Average loss: 0.0423, Accuracy: 9871/10000 (98.71%)

EPOCH:  3
loss=0.0693153440952301 batch_id=468: 100%|██████████| 469/469 [00:20<00:00, 23.36it/s]
Test set: Average loss: 0.0386, Accuracy: 9877/10000 (98.77%)

EPOCH:  4
loss=0.06488003581762314 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 23.56it/s]
Test set: Average loss: 0.0282, Accuracy: 9905/10000 (99.05%)

EPOCH:  5
loss=0.04795704782009125 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 24.46it/s]
Test set: Average loss: 0.0279, Accuracy: 9897/10000 (98.97%)

EPOCH:  6
loss=0.012918882071971893 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 24.43it/s]
Test set: Average loss: 0.0292, Accuracy: 9907/10000 (99.07%)

EPOCH:  7
loss=0.1106804609298706 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 23.95it/s]
Test set: Average loss: 0.0229, Accuracy: 9930/10000 (99.30%)

EPOCH:  8
loss=0.03011081926524639 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 23.57it/s]
Test set: Average loss: 0.0247, Accuracy: 9920/10000 (99.20%)

EPOCH:  9
loss=0.025550978258252144 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 23.78it/s]
Test set: Average loss: 0.0199, Accuracy: 9924/10000 (99.24%)

EPOCH:  10
loss=0.029175972566008568 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 24.54it/s]
Test set: Average loss: 0.0178, Accuracy: 9947/10000 (99.47%)

EPOCH:  11
loss=0.012265072204172611 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 24.54it/s]
Test set: Average loss: 0.0174, Accuracy: 9942/10000 (99.42%)

EPOCH:  12
loss=0.019355790689587593 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 23.72it/s]
Test set: Average loss: 0.0254, Accuracy: 9914/10000 (99.14%)

EPOCH:  13
loss=0.11313191801309586 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 23.72it/s]
Test set: Average loss: 0.0243, Accuracy: 9927/10000 (99.27%)

EPOCH:  14
loss=0.019127102568745613 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 24.35it/s]
Test set: Average loss: 0.0179, Accuracy: 9941/10000 (99.41%)

EPOCH:  15
loss=0.035972435027360916 batch_id=468: 100%|██████████| 469/469 [00:18<00:00, 24.75it/s]
Test set: Average loss: 0.0184, Accuracy: 9944/10000 (99.44%)

EPOCH:  16
loss=0.004591097589582205 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 23.66it/s]
Test set: Average loss: 0.0179, Accuracy: 9944/10000 (99.44%)

EPOCH:  17
loss=0.01865175925195217 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 23.58it/s]
Test set: Average loss: 0.0169, Accuracy: 9940/10000 (99.40%)

EPOCH:  18
loss=0.025008955970406532 batch_id=468: 100%|██████████| 469/469 [00:20<00:00, 23.24it/s]
Test set: Average loss: 0.0210, Accuracy: 9929/10000 (99.29%)

EPOCH:  19
loss=0.01065506786108017 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 24.65it/s]
Test set: Average loss: 0.0151, **Accuracy: 9949/10000 (99.49%)**

EPOCH:  20
loss=0.005859756376594305 batch_id=468: 100%|██████████| 469/469 [00:19<00:00, 24.61it/s]
Test set: Average loss: 0.0162, Accuracy: 9946/10000 (99.46%)


Test set: Average loss: 0.0186, Accuracy: 9934/10000 (99.34%)

