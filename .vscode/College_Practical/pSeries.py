import pandas as pd
import numpy as np
l1 = pd.Series([6,4,3,1])
print(l1)
l2 = pd.Series([6,7,8,9,10])
print(l2)

print("Addition of two series:",l1+l2)
print("Subtraction of two series:",l1-l2)
print("Multiplication of two series:",l1*l2)
print("Division of two series:",l1/l2)

dict = {'a': 100, 'b': 200, 'c':300, 'd':400,
'e':800}

data = pd.Series(dict)
print(data)

data = np.array([23,45,67,89,12])
s = pd.Series(data)
print(s)

