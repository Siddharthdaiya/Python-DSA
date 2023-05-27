from array import *
import numpy as np
two_DArray=np.array([[15,10,13,18],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(two_DArray)

newtwoDarray=np.insert(two_DArray,0,[10,20,30,40],axis=0)
print(newtwoDarray)