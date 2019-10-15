# Notes on using python arrays:
# - Don't use them unless you are using homogenous C array for data
# https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use

import array as arr

# creating array
a = arr.array('i', [1, 2, 3])
print(a)

# accessing array
print("First element:", a[0])
print("Last element:", a[-1])

# slicing arrays
print("First 2 elements:", a[0:2])

# adding arrays
a.append(4) # Appends adds a single item
print(a)
a.extend([5, 6, 7]) # Extends adds an iterable at the end
print(a)

# delete arrays
del a[3]
print(a)

del a
# Should Throw an error here
print(a)
