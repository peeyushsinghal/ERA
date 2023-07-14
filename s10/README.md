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
