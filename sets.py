# Creating an empty set
empty_set = {}          # this is wrong as it creates an empty dictionary instead of a set
empty_set = set()
print(empty_set)

# they store elements which are unordered.
# Duplicates are not allowed in sets

fruits_set = {'mango','apple','banana','melon','apple'}

print(fruits_set)

# Sets are optimized for membership tests as well
print('apple' in fruits_set)        # although lists and tuple also support this feature but sets are more optimized for it

# Set operations
fruits_set_2 = {'apple','water melon','guava','grapes','oranges','melon'}
print('Elements which are common in both sets : ', fruits_set.intersection(fruits_set_2))
print('Elements which are present in set 1 but not in set 2 : ', fruits_set.difference(fruits_set_2))
print('All the elements in both sets : ', fruits_set.union(fruits_set_2))