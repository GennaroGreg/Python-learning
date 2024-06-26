# Tuples
my_tuple = tuple(('Greg', 42, True))
another_tuple = (1, 4, 2, 8)

print(my_tuple)
print(type(my_tuple))
print(type(another_tuple))

# Can't modify Tuple, so have to do to the following:
new_list = list(my_tuple) # Create new list from tuple
new_list.append('Percy') # Add value to list
new_tuple = tuple(new_list) # Create new tuple
print(new_tuple)

# Assign variables to tuple elements
(one, two, *three) = another_tuple
print(one)
print(two)
print(three)