import numpy as np

a =  np.arange(12).reshape(4,3)
b =  np.arange(24).reshape(6,4)


# If we wants to print only 1st, 3rd, 4th rows.
print(a)
print(a[[0,2,3]])

# If we wants to print 1st, 3rd, 4th, 6th rows.
print(b)
print(b[[0,2,3,5]])

# if we wants 1st, 2nd, 3rd columns.
print(b[:,[0,2,3]])
print(b[[3,4,5]])
print(b[:,[0,1]])
