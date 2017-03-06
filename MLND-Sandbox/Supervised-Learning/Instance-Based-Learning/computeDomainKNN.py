import numpy as np

feature_train = np.array([[1,6],[2,4],[3,7],[6,8],[7,1],[8,4]])
feature_label = np.array([7,8,16,44,50,68])

feature_test = np.array([[4,2]])
e = np.array([1,1])


# euclidean distance
print np.dot(np.power((feature_train-feature_test),2), e)
# manhattan distance
print np.dot(np.abs(feature_train-feature_test), e)

print float(feature_label[1])/1

print float(feature_label[1] + feature_label[4] + feature_label[5])/3

print float(feature_label[1]+feature_label[4])/2

print float(feature_label[1]+feature_label[4]+feature_label[2]+feature_label[5])/4

