import numpy as np
import math

def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)

    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module

    # TODO : need to code to calculate r^2 (coefficient of determination)
    x_bar = np.average(features_test)
    y_bar = np.average(pred)

    # r = np.sum((features_test - x_bar)*(pred - y_bar)) / math.sqrt(np.sum(np.power(features_test - x_bar, 2))*np.sum(np.power(pred - y_bar, 2)))
    # print r
    


    accuracy = clf.score(features_test, labels_test)
    return accuracy

