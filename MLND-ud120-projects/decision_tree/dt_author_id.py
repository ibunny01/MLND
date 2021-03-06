#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import os,sys
os.chdir(sys.path[0])

import sys
from time import time
sys.path.append("../tools/")
sys.path.append("../choose_your_own/")
from email_preprocess import preprocess
from class_vis import prettyPicture


from sklearn.naive_bayes import GaussianNB


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
# print features_train
# print labels_train

clf = GaussianNB()
clf.fit(features_train, labels_train)

print clf.predict(features_test)
print labels_test
# prettyPicture(clf,features_test, labels_test)


#########################################################


