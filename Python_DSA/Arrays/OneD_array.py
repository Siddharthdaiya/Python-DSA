from array import *

# Create an array and traverse it
my_array=array('i',[10,20,30,40,50])
for i in my_array:
    print(i)
    
# Accessing Individual Element from Array Throough Index
print("Step 2")
print(my_array[0])

# Append Any Value Using Append Method()
print("Step 3")
my_array.append(60)
print(my_array)

# Insert Any Value Using Insert Method()
print("Step 4")
my_array.insert(0,100)
print(my_array)

# Extend Any Value Using Extend Method()
print("Step 5")
my_array1=array('i',[70,80,90])
my_array.extend(my_array1)
print(my_array)

# Add items from List using FromList Method()
print("Step 6")
tempList=[110,120,130,140]
my_array.fromlist(tempList)
print(my_array)

# Remove element from array using Remove Method()
print("Step 7")
my_array.remove(100)
print(my_array)

# Remove element from array using POP Method()
print("Step 8")
my_array.pop()
print(my_array)

# Fetch any element through its index using Index Method()
print("Step 9")
print(my_array.index(90))

# Reverese An Array Using Reverse Function
print("Step 10")
my_array.reverse()
print(my_array)

# Count Occurence Of any Elemenrt using Count Method()
print("Step 11")
my_array.append(10)
print(my_array.count(10))
print(my_array)

# Slice Elements using slice method in array
print('Step 12')
print(my_array[::-1])
