import numpy as np
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

print(a1)
#last item -> Positive indexing
print(a1[-1])
#first item -> Negative indexing
print(a1[0])

print(a2)
#locate the 6
print(a2[1,2])
print(a2[2,3])
print(a2[1,0])

print(a3)
print(a3[1,0,1])
print(a3[0,1,0])
print(a3[0,0,0])
print(a3[1,1,0])