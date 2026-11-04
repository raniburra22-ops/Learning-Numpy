import numpy as np
a1 = np.random.random((3,3))
a1 = np.round(a1*100)

print(a1)
print("Maximum : ", np.max(a1))
print("Minimum : " ,np.min(a1))
print("Sum : " ,np.sum(a1))
print("Product : " ,np.prod(a1))

# take a number coloumn vise
print("Maximum : ", np.max(a1, axis= 0))
print("Minimum : " ,np.min(a1, axis=0))
print("Sum : " ,np.sum(a1, axis=0))
print("Product : " ,np.prod(a1, axis=0))

# take a number row vise
print("Maximum : ", np.max(a1, axis=1))
print("Minimum : " ,np.min(a1, axis=1))
print("Sum : " ,np.sum(a1, axis=1))
print("Product : " ,np.prod(a1, axis=1))
