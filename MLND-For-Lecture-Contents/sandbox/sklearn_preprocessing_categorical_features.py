#http://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-categorical-features

from sklearn import preprocessing
import numpy as np

enc = preprocessing.OneHotEncoder()
print enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])  
print enc.transform([[0, 1, 3]]).toarray()

enc = preprocessing.OneHotEncoder(n_values=[2, 3, 4])
# Note that there are missing categorical values for the 2nd and 3rd
# features
print enc.fit([[1, 2, 3], [0, 2, 0]])  
print enc.transform([[1, 0, 0]]).toarray()