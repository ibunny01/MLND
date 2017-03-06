from math import sqrt

#data = [199, 200, 201, 202, 203, 204, 205, 206]

data = [21]*4+[24]*6+[26]*7+[29]*11+[40]*2

datax=[6, 2, 1, -1]
datay=[7,3,2,0]

datax2 = range(0,10) + [1000]
datay2 = [0]*10 + [1000]


datax3 = [1,2,3]
datay3 = [4,7,13]


dx4 = [70,57,63,70,53,75,58]
dy4 = [1,1,1,1,2,2,1]


def mean(d):
    return float(sum(d))/len(d) 

def var(d):
    mu=mean(d)
    newdata=[(x-mu)**2 for x in d]
    return mean(newdata)

def stddev(d):
    return sqrt(var(d))

def compute_ci(d):
    return sqrt(var(d)/len(d))

print mean(data)
print var(data)
print stddev(data)

print compute_ci(data)


print 1.96*compute_ci(data)

# if # of data is not enough to fit gaussian distribution (N>=30), we have to choose value of t-distributions
print 2.0452*compute_ci(data)


print mean(datax)
print mean(datay)

mux = mean(datax)
muy = mean(datay)

print mux
print muy

print float(sum([(nx-mux) * (ny-muy) for (nx, ny) in zip(datax, datay)])) 
print float(sum([(nx - mux)**2 for nx in datax]))


print [(nx-mux) * (ny-muy) for (nx, ny) in zip(datax, datay)]
print [(nx - mux)**2 for nx in datax]


dataxy2 = zip(datax2, datay2)

print dataxy2 

mux2 = mean(datax2)
muy2 = mean(datay2)

print mux2, muy2

newdataxy2 = [(nx - mux2, ny - muy2) for (nx, ny) in dataxy2]

print sum([(nx - mux2)*(ny - muy2) for (nx, ny) in dataxy2]) / sum([(nx - mux2)**2 for (nx, ny) in dataxy2])


dataxy3 = zip(datax3, datay3)

mux3 = mean(datax3)
muy3 = mean(datay3)

print dataxy3
print mux3, muy3

print sum([(nx - mux3)*(ny - muy3) for (nx, ny) in dataxy3]) / sum([(nx - mux3)**2 for (nx, ny) in dataxy3])

print sum([(nx - mux3)*(ny - muy3) for (nx, ny) in dataxy3]) / sqrt(sum([(nx - mux3)**2 for (nx, ny) in dataxy3]) * sum([(ny - muy3)**2 for (nx, ny) in dataxy3]))

print round(-6.972285166477 * 10**-5, 10)


dxy4 = zip(dx4,dy4)

print dxy4

mux4 = mean(dx4)
muy4 = mean(dy4)

print mux4, muy4

b = sum([(nx - mux4)*(ny-muy4) for (nx,ny) in dxy4]) / sum([(nx-mux4)**2 for (nx, ny) in dxy4])
print b

a = muy4 - (sum([(nx - mux4)*(ny-muy4) for (nx,ny) in dxy4]) / sum([(nx-mux4)**2 for (nx, ny) in dxy4]))*mux4
print a

print sum([(nx)**2 for (nx,ny) in dxy4])

print sum([(nx*ny) for (nx,ny) in dxy4])

print b*36+a

print (574.0 - 1600*9/23) / (112400 - 1600**2 / 23)

print 9.0/23 - ((574.0 - 1600*9/23) / (112400 - 1600**2 / 23)) * 1600/23

print 36 * ((574.0 - 1600*9/23) / (112400 - 1600**2 / 23)) + (9.0/23 - ((574.0 - 1600*9/23) / (112400 - 1600**2 / 23)) * 1600/23)


print (1.0/12)+ (1.0/16)

print ((1.0/12)) / ((1.0/12)+ (1.0/16))

print 21 * (0.2)**2 * (0.8)**5

print 1 - (0.8**7) - (7* 0.2* 0.8**6)


print sqrt(1.25)


print 70*2.54, 25*(2.54)**2


print 0.495*(1-0.495)

print 0.495 - 1.645*sqrt(0.495*(1-0.495) / 10000)
print 0.495 + 1.645*sqrt(0.495*(1-0.495) / 10000)

print 1.28*sqrt(0.495*(1-0.495) / 10000)

dx5 = [0.79,0.70,0.73,0.66,0.65,0.70,0.74,0.81,0.71,0.70]
mux5 = sum(dx5) / len(dx5)

ci = 1.96*sqrt(sum([(nx-mux5)**2 for nx in dx5]) / len(dx5)) / sqrt(len(dx5))

print mux5 - ci, mux5 + ci