users = ['Greg', 'Cody', 'Percy'] # List! Not array

data = ['Greg', 55, True]

emptyList = []

print("Greg" in emptyList)

print(users[0]) # First element
print(users[-1]) # Last element

print(users.index('Greg')) # Return element that matches query

print(len(data)) # Length

users.append('Miggy')
print(users)

users += ['Matthew', 'Chris', 'Neeraj']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Jeff'] # Adds values at designated index (2)
print(users)

users[1:3] = ['Sam', 'Saul'] # Replace values in designated range
print(users)

users.remove('Bob')
print(users)

print(users.pop()) # Returns last value in list
print(users)

del users[0] # Delete user at designated index
print(users)

users[1:2] = ['dave'] # Lowercase comes after Uppercase
users.sort()
print(users)

users.sort(key = str.lower)
print(users)


users.clear() # Clears list, does not delete
print(users)

# del data
# Should return undefined in next line!
# print(data)

nums = [4, 42, 78, 1, 5]
nums.reverse() # Backwards
print(nums)

# nums.sort(reverse=True) # Descending order
# print(nums)

print(sorted(nums, reverse=True)) # Does not alter input nums
print(nums)

# Copy List
nums_copy = nums.copy()
my_nums = list(nums)
nums_copy_1 = nums[:] # full slice

print(nums_copy)
print(my_nums)
nums_copy_1.sort()
print(nums_copy_1)
print(nums)

# Check type
print(type(nums))

new_list = list([1, "Greg", True]) # Constructor function
print(new_list)
