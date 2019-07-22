# List data structure

# empty list
myList = []

# list of integers
intList = [1,2,3]

# list with mixed datatypes
mixedList = [1, "Hello", 3.4]

print(myList)
print(intList)
print(mixedList)

# Nested list , list inside another list
nestedList = ["mouse", [8,4,6], ["a"]]
print(nestedList)

# Accessing lists 
# normal list, normal indexing
myList = ["h", "e", "l", "l", "o"]
print("Index 0 of list = ", myList[0])

# Nested list, nested indexing
nestedList = ["Happy", [2,0,1,5]]
# Second value of first value
print(nestedList[0][1])

#Fourth value of second value
print(nestedList[1][3])


# Negative indexing
# -1 is the last value, -2 is the second last value, and so on...
print(myList[-1])

# Slicing lists
print(myList[3:5])

print(myList[3:])

print(myList[:])

# Changing values of a list
# lists are mutable, can change its values
odd = [2,4,6,8]
print(odd)
# change 1st item
odd[0] = 1
print(odd)

# change 2nd to 4th items
odd[1:4] = [3,5,7]
print(odd)


# Append method to add one item to a list
odd.append(9)
print("append: ", odd)

# Extend to add multiple items to a list
odd.extend([11, 13, 15])
print("extend: ", odd)

# Combine lists using + operator
odd = [1,3,5]
print(odd + [9,7,5])

# * operator to repeat a list for the set number of times
print(odd * 3)

# Insert an item in a desired place in a list with Insert method
odd = [1,2]
odd.insert(1,3)
print(odd)

odd[2:2] = [5,7]
print(odd)

# Remove or delete list elements
myList = ["p", "r", "o", "b", "l", "e", "m"]
#delete one item
del myList[2]
print(myList)

# delete multiple items
del myList[1:5]
print(myList)

# delete entire list
del myList
#print(myList)

# Use remove() to remove a given item
myList = ["p", "r", "o", "b", "l", "e", "m"]

myList.remove("p")
print(myList)

# Use pop() to get rid of an item at the given index
# removes and returns the final item of the list if the index is not given
# Help us implement stacks (first in last out)
myList.pop(1)
print(myList)

myList.pop()
print(myList)

# To empy a list you can use clear() method
myList.clear()
print(myList)

# You can also delete items by allocating an empty list to a slice of elements
myList = ["p", "r", "o", "b", "l", "e", "m"]
myList[2:3] = []
print(myList)

myList[2:5] = []
print(myList)

# -------> PYTHON LIST METHODS <-----------
# append() - add some element to the end of the list
# extend() - add all list elements to the another list
# insert() - insert an item at the set index
# remove() - remove an item from your list
# pop() - remove and return some element of a given list - if index is not passed then return the last index - like a stack
# clear() - remove all items from the list
# index() - return the first matched item's index
# count() - count number of elements of given list
# sort() - sort all items in ascending order
# reverse() - reverse the list's order of items

myList = [3,8,1,6,0,8,4]
print(myList)
print("index(8): ", myList.index(8))
myList.sort()
print("Sorted ascending: ", myList)
myList.reverse()
print("List reversed: ", myList)

# LIST COMPREHENSION - create lists
