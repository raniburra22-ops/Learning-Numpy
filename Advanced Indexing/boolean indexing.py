import numpy as np
a = np.random.randint(1,100,24).reshape(6,4)
print(a)

# Find all numbers greater than 50
print(a>50)
print(a[a>50])

# Find out even number
print(a % 2 == 0)
print(a[a % 2 == 0])

# Find all number greater than 50 and are even
print((a>50) & (a % 2 == 0))
print(a[(a>50) & (a % 2 == 0)])

# Find all number  divisible by 7
print(a[a % 7 == 0])
