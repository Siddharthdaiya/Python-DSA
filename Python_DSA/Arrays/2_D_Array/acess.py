from array import *
import numpy as np
two_DArray=np.array([[15,10,13,18],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(two_DArray)
def acess_twoD_array(array,rowIndex,collIndex):
    if rowIndex>=len(array) and collIndex>=len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][collIndex])
acess_twoD_array(two_DArray,1,3)