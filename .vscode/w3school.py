import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
print(x)
y = np.median(speed)
print(y)

z = stats.mode(speed)
print("Value of mode:",z)
speed1 = [86,87,88,86,87,85,86]

# Standard deviation is a number that describes how spread out the values are.

# A low standard deviation means that most of the numbers are close to the mean (average) value.

# A high standard deviation means that the values are spread out over a wider range.

derivation = np.std(speed1)
print(derivation) #low standard darivation because values are less spread out

# Variance is another number that indicates how spread out the values are.

# In fact, if you take the square root of the variance, you get the standard deviation!

# Or the other way around, if you multiply the standard deviation by itself, you get the variance!

variance = np.var(speed)
print(variance)
d = np.std(speed)
print(d)

# Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

num = np.percentile(ages,75)
print(num)


# To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size

data1 = np.random.uniform(0,50,240)
data2 = np.random.uniform(0,50,240)
a = np.std(data1)
print(a)
plt.hist(data1,50)
plt.show()

plt.scatter(data1,data2)
plt.show()

#linearr egression 

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope,intercept,r,p,std_err = stats.linregress(x,y)

def func(x):
    return slope * x + intercept

model = list(map(func,x))
print(r)
plt.scatter(x,y)
plt.plot(x,model)
plt.show()


x1 = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y1 = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope1,intercept1,r1,p1,std_err = stats.linregress(x1,y1)

def func1(x1):
    return slope1 * x1 + intercept1

model = list(map(func1,x1))
print("Value of relation1:",r1)
plt.scatter(x1,y1)
plt.plot(x1,model)
plt.show()