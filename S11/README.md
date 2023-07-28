Objective
---------

Train ResNet18 on Cifar10 for 20 Epochs. The assignment must:
- pull your Github code to google colab (don't copy-paste code)
-  prove that you are following the structure https://github.com/kuangliu/pytorch-cifar (delete bottleneck layer)
-  that the code in your google collab notebook is NOTHING.. barely anything. There should not be any function or class that you can define in your Google Colab Notebook. Everything must be imported from all of your other files
-  your colab file must:
  -   rain resnet18 for 20 epochs on the CIFAR10 dataset
  -   show loss curves for test and train datasets
  -   show a gallery of 10 misclassified images
  -   show gradcamLinks to an external site. output on 10 misclassified images. 
-  Once done, upload the code to GitHub, and share the code. This readme must link to the main repo so we can read your file structure. 
-  Train for 20 epochs
-  Get 10 misclassified images
-  Get 10 GradCam outputs on any misclassified images (remember that you MUST use the library we discussed in the class)
-  Apply these transforms while training:
  -   RandomCrop(32, padding=4)
  -   CutOut(16x16)

Training Plots
--------------
![image](https://github.com/peeyushsinghal/ERA/assets/10797988/d78d2573-5d77-45bf-8365-25a9aa682795)
![image](https://github.com/peeyushsinghal/ERA/assets/10797988/a3a1d4fb-cbac-4a18-bd98-6ab61b87f9ba)


Misclassified Images
--------------
![image](https://github.com/peeyushsinghal/ERA/assets/10797988/d8bf8a25-9697-4cac-ac80-8eca5e3c8396)

GradCam on Misclassified Images
-------------------------------
![image](https://github.com/peeyushsinghal/ERA/assets/10797988/bb33ee1e-473a-4ca3-9d16-bdc5ad39b8cc)

