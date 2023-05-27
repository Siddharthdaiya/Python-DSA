import array
from array import *
arr1=array('i',[10,32,52,10,450])
def access_array(array,index):
    if index >= len(array):
        print("There is no such Element in the array..........")
    else:
        print(array[index])
access_array(arr1,2)