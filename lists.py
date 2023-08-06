# It allows us to work with sequential data

# Creating a list
courses = ['AI','Cybersecurity','DevOps','Cloud Computing']
print('List of courses : ',courses)

# We can access the individual elements of a list just like an array in java
# indexing in lists also starts from 0
# If we try to fetch an element at an index which doesn't exists in the list, then we get the IndexError
print('Fetching the element at index 2 from courses : ', courses[2])

# Fetching the last element of the list
print('Fetching the last element of the list courses : ', courses[len(courses) - 1])        # using len() method 
print('Fetching the last element of the list courses : ', courses[-1])                      # using negative indexing
# by using negative indexing as -1, we don't need to worry about the number of elements in the list as it always returns the last element of the list

# Fetching a range of values from the list via slicing in the range [startIdx, endIdx)
print('Fetching the range of values in range [0,2)', courses[0:2])
print('Fetching all the values of the list till index 2', courses[:2])
print('Fetching all the values of the list from index 2', courses[2:])

# Adding an elememnt to the end of the list
courses.append('Big Data')
print('List after appending "Big Data" : ', courses)

# Adding an element to a particular location in the list using insert(index, value) method
courses.insert(0, 'Data Science')
print('List after adding "Data Science" at the start : ', courses)

# To add the elements from other list, we can use the extend() method
courses_2 = ['Java','Python']
courses.extend(courses_2)
print('List after extend() mehtod : ', courses)

# If we use append() or insert() method, then instead of adding the individual elements from 2nd list, it adds the 2nd list entirely as an element
courses.append(courses_2)
print('List after append() mehtod : ', courses)

# removing an element from the end of the list using pop() method
popped_element = courses.pop()
print('List after popping the last element using pop() mehtod : ', courses)
print('Popped element : ', popped_element)

# removing an first occurrence of any element in the list using remove() method
# it raises an error if the element is not present in the list
courses.append('AI')
print('Updated list : ', courses)
courses.remove('AI')
print('Updated list after remove() method : ', courses)

# to reverse the list in place, use reverse() method
courses.reverse()
print('List after reversing : ', courses)

# to avoid sorting the list in place, use sorted() function
# it returns a sorted version of list
sorted_courses = sorted(courses)
print('Sorted list : ', sorted_courses)

# to sort the list in place, use sort() method
# in case of numeric data, the default sorting order is ascending order
# we can sort in descending order too by using the sort(reverse = True) attribute
courses.sort()
print('Sorted list is ascending order : ', courses)
courses.sort(reverse = True)
print('Sorted list in descending order : ', courses)

# to find the min, max and sum of values in the list, use min(), max() and sum() function respectively
nums = [6,3,9,4,1,8,6,4,5]
print('Min element of list : ', min(nums))
print('Max element of list : ', max(nums))
print('Sum of elements of list : ', sum(nums))

# to find the first index of any element in the list, use index() method
# if that element doesn't exists in the list, we get an error
print('Index of "Big Data" in the list courses : ', courses.index('Big Data'))

# to check if any element exists in our list, we use the 'in' operator
print('Is "AI" present in courses : ', 'AI' in courses)
print('Is "ML" present in courses : ', 'ML' in courses)

# We can iterate/loop over our list using the for loop
print('--------------------------------------------')
print('Iterating over the courses list : ')

for idx in range(len(courses)):         # approach 1
    print(idx, courses[idx])

print('--------------------------------------------')

for course in courses:                  # approach 2
    print(course)

# to fetch the index and value simultaneously, we use the enumerate() function
print('--------------------------------------------')
print('Idx', 'Values')
for idx, course in enumerate(courses):
    print(idx, course)

# by default, the starting index is taken as 0, to set it to some other value, we can use the start attribute of enumerate() function
print('--------------------------------------------')
print('Idx(starting index = 1)', 'Values')
for idx, course in enumerate(courses, start=1):
    print(idx, course)

# to join all the elements of the list as a string (separated by comma), use the join() method of string class
courses_str = ', '.join(courses)
print('List joined as a string via ", " as delimiter : ', ', '.join(courses))
print('List joined as a string via " - " as delimiter : ', ' - '.join(courses))

# we can create a list from a string using the split(delimeter) method
courses_list = courses_str.split(', ')
print('String converted into list : ', courses_list)


