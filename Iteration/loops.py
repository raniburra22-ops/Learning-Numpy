import numpy as np
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

print(a1)
for i in a1:
    print(i)

print(a2)
for i in np.nditer(a2):
    print(i)

print(a3)
for i in np.nditer(a3):
    print(i)