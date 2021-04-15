"""
Arrays (Lists), Dictionaries, Sets, Class Instances are mutable (can change)
Intergers, Tuples, Strings are immutable (can't change)
"""

arr_1 = ['a', 'b', 'c']
arr_2 = arr_1
arr_3 = arr_1.copy()

# print( arr_1 is arr_2) # True - identical pointer (stored memory)
# print( arr_1 is arr_3) # False - brand new pointer (stored memory) -- equal but not identical

# print(id(arr_1))
# print(id(arr_2))

# print(2 is 2)
# print(id(2))

# arr_2.append('d')

# print(arr_1)
# print(arr_2)
# print(arr_3)