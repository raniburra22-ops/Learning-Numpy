#--------------Formula of MSE---------------#
'''                 1
             MSE = --- submition(Yi - Yi^)^2
                    n
'''
import numpy as np
actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)
print(actual)
print(predicted)

# Loss Function
def mse(actual,preticted):
    return np.mean((actual - predicted)**2)
print(mse(actual,predicted))