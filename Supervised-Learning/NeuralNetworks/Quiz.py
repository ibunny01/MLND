import numpy as np


input = np.array([1,2,3])

wi1 = np.array([1,1,-5])
wi2 = np.array([3,-4,2])
wh1 = np.array([2,-1])

wio1 = np.dot(wi1, input)
print wio1
wio2 = np.dot(wi2, input)
print wio2

input2 = [wio1, wio2]
print input2

who1 = np.dot(wh1, input2)
print who1