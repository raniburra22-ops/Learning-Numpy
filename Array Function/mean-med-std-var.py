import numpy as np
#Statistic
a1 = np.random.random((3,3))
a1 = np.round(a1*100)

print(a1)
print("Mean : ", np.mean(a1))
print("Median : " ,np.median(a1))
print("Standard Deviation : " ,np.std(a1))
print("Variance : " ,np.var(a1))
