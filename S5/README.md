# Session 5 Outline 
- Re-look at the code that we worked on in Assignment 4 (the fixed version).
- Move the contents of the code to the following files:
    - model.py
    - utils.py
    - S5.ipynb

- Make the whole code run again. 
- Upload the code with the 3 files + README.md file (total 4 files) to GitHub. README.md (look at the spelling) must have details about this code and how to read your code (what file does what). Heavy negative scores for not formatting your markdown file into p, H1, H2, list, etc. 
- Attempt Assignment 5. 

## Usage

### S5.ipynb
- Overarching orchestrator
- Imports all required librarires
- Uses functions from utils and models
- Provides interface to look at results / training 
- Imports the files using 
  -  ``` git clone https://github.com/peeyushsinghal/ERA.git ```


### model.py
- Includes the main model file (inherits from nn.Module)

### utils.py
- Includes utility functions like
    - Getting Correct Count ```GetCorrectPredCount(pPrediction, pLabels)```
    - Training Function ```train(model, device, train_loader, optimizer, criterion)```
    - Test Function ```test(model, device, test_loader, criterion)```
    - Printing Loss and Accuracy for training and test

## How To Use
- Set GPU as the Hardware Accelerator
    - Google Colab - Runtime -> Change runtime type - > GPU
- Run All the code blocks of S5.ipynb
