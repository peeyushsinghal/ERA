Assignment
--------
Your new target is:
* 99.4% (this must be consistently shown in your last few epochs, and not a one-time achievement)
* Less than or equal to 15 Epochs
* Less than 8000 Parameters 
Do this in exactly 3 steps

Experiment 1
------------------------------------
**Objective / Target**

* Use Existing Initial Setup and Model
* Getting the model correct
* Very basic model
* Reduce the channel number throughout : Reduce capacity of model by reducing the number of channels

**Results**

* Parameters: 13658
* Best Train Accuracy: 99.1 %
* Best Test Accuracy: 99.31 %

**Analysis**

* Large but working model
* No overfitting
* Hovering about 99.25, best accuracy achieved for 1 epoch only

**Next Steps**

* Reduce Number of Params
* Apply Transformations

Experiment 2.x
------------------------------------
**Objective / Target**

* Increase capacity with params less than 8K
* Play with LR

**Results**

* Parameters: 7,900
* Best Train Accuracy: 98.94
* Best Test Accuracy: 99.25

**Analysis**

* Not Able to hit the accuracy mark
* Overfitting (train - test accuracy) < 0 is largely containted, model underfits (Target not achieved)
* LR has played its role to move up the accuracy
* Number of params < 8K
* Adding params near output helped much, so did removing input

**Next Steps**

* Play with large LR

  Experiment 3
------------------------------------

**Objective / Target**
* Play with LR

**Results**

* Parameters: 7,900
* Best Train Accuracy: 98.91
* Best Test Accuracy: 99.31

**Analysis**

* Not Able to hit the accuracy mark
* Overfitting (train - test accuracy) < 0 is largely containted, model underfits (Target not achieved)
* LR has played its role to move up the accuracy
* Number of params < 8K
* Adding params near output helped much, so did removing input

**Next Steps**

* Play with large LR /Submit
