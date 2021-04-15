"""
Arrays (Lists)

Static Array vs. Dynamic Array

Key difference between the is that dynamic can resize. For static arrays, you will have to set the size of the array.

Python uses dynamic arrays.

Indexes point to the start of the arrays.
"""

arr = [1,2,3,4]

# Access is O(1) (its just an addition operation)
print(arr[2])
print(arr[0])

# deleting is O(n)

# for static arrays
# O(n)
arr.append(5)

# for dynamic arrays
# O(1)
arr.append(6)