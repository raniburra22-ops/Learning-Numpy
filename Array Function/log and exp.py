import numpy as np
a1 = np.random.random((3,3))
a1 = np.round(a1*100)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)

print("log function : ", np.log(a1))
print("Exponents : ", np.exp(a1))