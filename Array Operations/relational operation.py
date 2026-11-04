import numpy as np

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12, 24).reshape(3,4)

print(a2 > 25)
print(a2 > 5)
print(a2 > 15)
print(a1 == 5)