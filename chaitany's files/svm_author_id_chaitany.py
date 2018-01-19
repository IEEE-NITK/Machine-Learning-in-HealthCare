#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm

clf = svm.SVC(kernel='rbf',C=10000)

t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
sara=0
chris=0
pred=clf.predict(features_test)
for element in range(len(pred)):
    if pred[element]==1:
        sara+=1
    else:
        chris+=1
print "training time:", round(time()-t1,3), "s"
from sklearn.metrics import accuracy_score
a= accuracy_score(pred,labels_test)

print a
print sara,chris

#########################################################


