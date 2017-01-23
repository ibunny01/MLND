from math import log
from scipy import stats

# print -0.5 * log(0.5, 2) + -0.5 * log(0.5, 2)
# print -2.0/3 * log(2.0/3, 2) + -1.0/3 * log(1.0/3, 2)

# print "entropy first child node = "+str(stats.entropy([2,1], base=2))
# print "entropy second child node = "+str(stats.entropy([0,1], base=2))

# grade
print "case of grade"
print "infomation gain = " + str((1.0 - (3.0/4 * stats.entropy([2,1], base=2) + 1.0/4 * stats.entropy([0,1], base=2) ) ))


# bumpiness
print "case of bumpiness"
print "infomation gain = " + str((1.0 - (2.0/4 * stats.entropy([1,1], base=2) + 2.0/4 * stats.entropy([1,1], base=2) ) ))

# speed limit 
print "case of speed limit"
print "infomation gain = " + str((1.0 - (2.0/4 * stats.entropy([2,0], base=2) + 2.0/4 * stats.entropy([2,0], base=2) ) ))
