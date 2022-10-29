from array import *
from re import I
stu_roll = array('i',[101,102,103,104,105]) # "i" is type code
for element in stu_roll:
    print(element)
    # *** OR ***
n=len(stu_roll)
for element in range(n):
    print(element)
# *** Array using while loop ***
i=0
while i<n:
    print(stu_roll[i])
    i+=1

# **** Apend ***
stu_roll.append(106)
stu_roll.append(107)
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1

# inserrt(2,103) Method => this method is used to insert the element in a perticular position of existing array
# ex array_name.insert(posion_number,new_number)

# pop() => this method removes last element of array
# ex : stu_roll.pop(index position)

# remove() method => use to remove specific element
# ex : stu_roll.remove(101)

# index() => returns the index position element
# ex : array_name.index(element) if element = 101 then O/P => 0

# reverse () => reverse the elements
# ex : stu_roll.reverse() 

# extend () => Append the two array
# ex : stu_roll.extend(arr) (arr = 2nd array name
# )