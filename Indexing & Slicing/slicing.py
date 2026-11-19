import numpy as np
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

print(a1)
# Slicing with 1D array
print(a1[2:5])
# Alternate slicing
print(a1[2:9:2])

print(a2)
# In 2D arry we want first row
print(a2[0,:])
# We want third column
print(a2[:,2])
# We want [5,6],[9,10]
print(a2[1:,1:3])
# We want [0,3],[8,11]
print(a2[::2,::3])
# We want [1,3],[9,11]
print(a2[::2,1::2])
# We want [4,7]
print(a2[1,::3])
# We want [1,2,3],[5,6,7]
print(a2[0:2,1:])

print(a3)
# We want second 2D array in 3D array
print(a3[1])
# We want first 2D array and third 2D array in 3D array
print(a3[::2])
# We want first row of firt 2D array 
print(a3[0,1,:])
# We want second column of second 2D array
print(a3[1,:,1])
# We want [22,23], [25,26]
print(a3[2,1:,1:])
# We want [0,2],[18,20]
print(a3[::2,0,::2])