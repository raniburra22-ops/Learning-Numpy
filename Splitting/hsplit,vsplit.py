import numpy as np
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)
a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)

# Horizontal Splitting
print(np.hsplit(a4,2))
print(np.hsplit(a4,4))

# Vertical Splitting
print(np.vsplit(a5,3))