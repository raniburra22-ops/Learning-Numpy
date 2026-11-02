import numpy as np
a = np.arange(8).reshape(2, 2, 2)
print(a.dtype)
a = a.astype(np.int16)
print(a.dtype)