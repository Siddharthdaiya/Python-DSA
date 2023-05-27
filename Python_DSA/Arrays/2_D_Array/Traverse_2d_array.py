from array import *
import numpy as np
two_DArray=np.array([[15,10,13,18],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(two_DArray)

def travese_array(array):
    for i in range(len(array) ):
        for j in range(len(array[0])):
            print(array[i][j])
travese_array(two_DArray)