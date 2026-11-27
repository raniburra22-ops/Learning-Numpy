import numpy as np
a = np.array([1,2,3,4,np.nan,6])
print(a)
# Showing missing value in boolean form 
print(np.isnan(a))
#Showing 
print(a[~np.isnan(a)])