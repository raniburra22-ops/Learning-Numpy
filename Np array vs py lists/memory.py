# How many memory occupies a python list.
a = [i for i in range(10000000)]
import sys
print(sys.getsizeof(a))

# How many memory occupies a numpy array.
import numpy as np
b = np.arange(10000000,dtype=np.int32)
print(sys.getsizeof(b))