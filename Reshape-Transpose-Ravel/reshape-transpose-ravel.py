import numpy as np
a1 = np.arange(10)

# Reshape
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

print(a2)
# Transpose
print(np.transpose(a2))

# Ravel -> covertinf into 1D array
print(a2.ravel())

print(a3.ravel())