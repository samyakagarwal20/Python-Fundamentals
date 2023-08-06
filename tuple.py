# Creating an empty tuple
empty_tuple = ()
empty_tuple = tuple()
print(empty_tuple)

# Like list, it also deals with the sequence of data
# Unlike list which are mutable, tuples are immutables
# Immutability means that once a tuple is created, we can't change its contents
# but its possible to assign a new value entirely to that tuple

list_1 = ['mango','banana','melon']
list_2 = list_1
print('List 1 : ',list_1)
print('List 2 : ',list_2)

list_1[2] = 'apple'
print('List 1 (after modifying list_1[2]) : ',list_1)
print('List 2 (after modifying list_1[2]) : ',list_2)

# changing the element of one list also changed the element of the other list
# this shows that mutability of list

tuple_1 = ('mango','banana','melon')
tuple_2 = tuple_1
print('Tuple 1 : ',tuple_1)
print('Tuple 2 : ',tuple_2)

# tuple_1[2] = 'apple'    # this statement throws an error as the elements of tuple can't be modified

# Therefore, if we need to iterate some data structure and modify it as well, we should go for list else go for tuple
# Since, tuples are immutable, thus, there are lesser methods for tuple as compared to lists


