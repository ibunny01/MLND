def classify(features_train, labels_train):
    
    ### your code goes here--should return a trained decision tree classifer
    from sklearn import tree
    
    clf = tree.DecisionTreeClassifier()           # min_sample_split deault value is 2 

    clf = tree.DecisionTreeClassifier(min_samples_split=50)
    clf.fit(features_train, labels_train)

    return clf