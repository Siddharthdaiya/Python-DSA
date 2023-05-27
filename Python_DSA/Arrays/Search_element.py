import array
from array import * 
# We are going to Use Linear search
arr1=array('i',[110,32,52,10,450])

def linear_search(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return -1
print(linear_search(arr1,10))
    