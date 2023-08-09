Assignment
- Move your S10 assignment to Lightning first and then to Spaces such that:
  -  (You have retrained your model on Lightning)
  -  You are using Gradio
  -  Your spaces app has these features:
    -  ask the user whether he/she wants to see GradCAM images and how many, and from which layer, allow opacity change as well
    -  ask whether he/she wants to view misclassified images, and how many
    -  allow users to upload new images, as well as provide 10 example images
    -  ask how many top classes are to be shown (make sure the user cannot enter more than 10)
  -  Add the full details on what your App is doing to Spaces README 
-  Head over to submissions and then:
  -  Submit the Spaces App Link
  -  Submit the Spaces README link (Space must not have a training code)
  -  Submit the GitHub Link where Lightning Code can be found along with detailed README with log, loss function graphs, and 10 misclassified images

---------------------------
Model Summary
------
```
INFO:pytorch_lightning.callbacks.model_summary:
   | Name                  | Type               | Params
--------------------------------------------------------------
0  | PrepLayer             | Sequential         | 1.9 K 
1  | PrepLayer.0           | Conv2d             | 1.8 K 
2  | PrepLayer.1           | BatchNorm2d        | 128   
3  | PrepLayer.2           | ReLU               | 0     
4  | Layer1                | LayerBlock         | 74.1 K
5  | Layer1.layer_block    | Sequential         | 74.1 K
6  | Layer1.layer_block.0  | Conv2d             | 73.9 K
7  | Layer1.layer_block.1  | MaxPool2d          | 0     
8  | Layer1.layer_block.2  | BatchNorm2d        | 256   
9  | Layer1.layer_block.3  | ReLU               | 0     
10 | resblock1             | ResBlock           | 295 K 
11 | resblock1.res_block   | Sequential         | 295 K 
12 | resblock1.res_block.0 | Conv2d             | 147 K 
13 | resblock1.res_block.1 | BatchNorm2d        | 256   
14 | resblock1.res_block.2 | ReLU               | 0     
15 | resblock1.res_block.3 | Conv2d             | 147 K 
16 | resblock1.res_block.4 | BatchNorm2d        | 256   
17 | resblock1.res_block.5 | ReLU               | 0     
18 | Layer2                | LayerBlock         | 295 K 
19 | Layer2.layer_block    | Sequential         | 295 K 
20 | Layer2.layer_block.0  | Conv2d             | 295 K 
21 | Layer2.layer_block.1  | MaxPool2d          | 0     
22 | Layer2.layer_block.2  | BatchNorm2d        | 512   
23 | Layer2.layer_block.3  | ReLU               | 0     
24 | resblock2             | ResBlock           | 1.2 M 
25 | resblock2.res_block   | Sequential         | 1.2 M 
26 | resblock2.res_block.0 | Conv2d             | 590 K 
27 | resblock2.res_block.1 | BatchNorm2d        | 512   
28 | resblock2.res_block.2 | ReLU               | 0     
29 | resblock2.res_block.3 | Conv2d             | 590 K 
30 | resblock2.res_block.4 | BatchNorm2d        | 512   
31 | resblock2.res_block.5 | ReLU               | 0     
32 | Layer3                | LayerBlock         | 1.2 M 
33 | Layer3.layer_block    | Sequential         | 1.2 M 
34 | Layer3.layer_block.0  | Conv2d             | 1.2 M 
35 | Layer3.layer_block.1  | MaxPool2d          | 0     
36 | Layer3.layer_block.2  | BatchNorm2d        | 1.0 K 
37 | Layer3.layer_block.3  | ReLU               | 0     
38 | resblock3             | ResBlock           | 4.7 M 
39 | resblock3.res_block   | Sequential         | 4.7 M 
40 | resblock3.res_block.0 | Conv2d             | 2.4 M 
41 | resblock3.res_block.1 | BatchNorm2d        | 1.0 K 
42 | resblock3.res_block.2 | ReLU               | 0     
43 | resblock3.res_block.3 | Conv2d             | 2.4 M 
44 | resblock3.res_block.4 | BatchNorm2d        | 1.0 K 
45 | resblock3.res_block.5 | ReLU               | 0     
46 | max_pool4             | MaxPool2d          | 0     
47 | fc                    | Linear             | 5.1 K 
48 | criterion             | CrossEntropyLoss   | 0     
49 | train_accuracy        | MulticlassAccuracy | 0     
50 | val_accuracy          | MulticlassAccuracy | 0     
--------------------------------------------------------------
7.8 M     Trainable params
0         Non-trainable params
7.8 M     Total params
31.026    Total estimated model params size (MB)
```


Model Metrics
-------
- LR
  
![image](https://github.com/peeyushsinghal/ERA/assets/10797988/bfa24740-5ab2-47ee-a271-843516eed075)
- VAL Accuracy
  
  ![image](https://github.com/peeyushsinghal/ERA/assets/10797988/1453e01b-cc8f-4b75-b0f0-7c80b03f7dc9)

  ![image](https://github.com/peeyushsinghal/ERA/assets/10797988/9fd6e6b2-56cf-4553-ba11-d8cee709e33d)
-------
Misclassified Images
---------------
![image](https://github.com/peeyushsinghal/ERA/assets/10797988/5becbe3d-c951-4420-8d10-f55c9f4ba85d)

GradCAM IMages
--------------
![image](https://github.com/peeyushsinghal/ERA/assets/10797988/70d17381-51b0-49de-ad59-043f7dd7766e)

