# Calculate the speed of python list.
a = [i for i in range(10000000)]
b = [i for i in range(10000000,20000000)]

c = []
import time

start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])
print(time.time()-start)    

# Calculate the speed of numpy array.
import numpy as np
d = np.arange(10000000)
e = np.arange(10000000,20000000)

start = time.time()
f = d + e
print(time.time()-start)