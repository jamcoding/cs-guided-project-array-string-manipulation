# Describe the difference between an in-place algorithm and an out-of-place algorithm

def in_place_double(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * 2

    return arr

# Works for dictionaries since it is a mutable object
# def in_place_add_key(dict):
#     dict['new_key'] = 2

# d = {'a': 1}

# in_place_add_key(d)
# print(d)

"""
Stick to out-of-place functions (Pure function). You won't have to worry about accidentally changing data
"""
def out_of_place_double(arr):
    # create new arr
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[i] * 2)

    return new_arr


arr_1 = [1,2,3,4,5]

# mutable objects get passed by reference
# arr_2 = in_place_double(arr_1)

# print(arr_2)
# print(arr_1)
# print(arr_2 is arr_1) # True


# arr_3 = out_of_place_double(arr_1)
# print(arr_3)
# print(arr_1)
# print(arr_3 is arr_1) # False

def append_string(string):
    string = string + " horray!"
    return string

# immutable objects gets passed by copy
str_1 = "Hip hip"
str_2 = append_string(str_1)

print(str_1)
print(str_2)