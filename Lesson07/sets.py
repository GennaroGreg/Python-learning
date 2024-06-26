# Sets
nums = {1,2,3,4}
nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed
nums = {1,2,2,3}
print(nums) # {1,2,3}

# True is a dupe is of 1, False is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums) # {False, 1, 2, 3, 4}

# Check if value exists in set
print(2 in nums)

# Cannot refer to element with index position or key

# Add new element to set
nums.add(8)
print(nums)

# Add elements from one set to another
nums3 = {5,6,7}
nums.update(nums3)
print(nums)

# Can use update with lists, tuples, dictionaries, sets

# Merge 2 sets to create new set
one = {1,2,3}
two = {5,6,7}
newSet = one.union(two) # Doesn't change originals
print(newSet)

# Keep only duplicates from 2 sets
one = {1,2,3}
two = {2,3,4}
one.intersection_update(two)
print(one)

# Keep everything except duplicates
one = {1,2,3}
two = {2,3,4}
one.symmetric_difference_update(two)
print(one)