from array import *
import numpy as np
two_DArray=np.array([[15,10,13,18],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(two_DArray)

def linear_search(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==value:
                return 'The Value is Located At '+str(i)+" "+str(j)
    return "The Element is Not Found......"
print(linear_search(two_DArray,110))