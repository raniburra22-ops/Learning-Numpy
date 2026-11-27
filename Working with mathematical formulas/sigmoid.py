#------------Formula of sigmoid------------------#
'''                      1
               S(x) = ----------
                      1 + e^(-x)
'''

import numpy as np

def sigmoid(array):
    return 1/(1+np.exp(-(array)))
a = np.arange(100)
print(sigmoid(a))