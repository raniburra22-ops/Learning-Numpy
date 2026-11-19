import numpy as np
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)
a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)

print(a4)
print(a5)

# Horizontal Stacking
print(np.hstack((a4,a5)))

# Vertical Stacking
print(np.vstack((a4,a5)))