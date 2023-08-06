# Dictionary stores the data as key-value pairs

# Craeting dictionary
student = {'name': 'Peter', 'age': 25, 'courses' : ['AI', 'Cybersecurity']}
print('Student details : ', student)

# We can access a particular key's value 
print('Student name : ',student['name'])
print('Student age : ',student['age'])

# If we try to fetch the data for a key which doesn't exists in the dictionary, we get a KeyError
# print(student['phone'])

# Generally, we would not like to directly throw an error, instead we would like to return something like null / none
# For this, we can get the data from the dictionary using get() method
print('Student name using get() : ', student.get('name'))

# By default, if the key doesn't exists and we fetch it using get() method, we get 'None' as result
print('Student phone using get() : ', student.get('phone'))

# We can also specify a custom value to be returned in such scenarios
print('Student email using get() : ', student.get('email','Not Found'))

# We can add a new entry into the dictionary as follows
student['phone'] = '9876543210'
print('Student phone using get() : ', student.get('phone', 'Not Found'))

# In case if the key already exists in the dictionary, the key is updated with the new value
student['name'] = 'Tony'
print('Student data : ', student)

# We can add / update multiple fields in the dictionary simultaneously using the update() method which accepts a dictionary type
details_to_update = {'name' : 'Barney', 'age': 28, 'phone': '1234567890'}
student.update(details_to_update)
print('Student details after update() : ', student)

# We can delete a particular key from the dictionary using the del keyword
del student['phone']
print('Student data after del : ', student)

# We can also achieve the same using pop() method. The difference is that it returns the popped value for that key
age = student.pop('age')
print('Student data after pop() : ', age)

# We can fetch the number of keys in the dictionary using len() function
print('No of keys in dictionary : ', len(student))

# To see all the keys in the dictionary, we use keys() method
print('Dictionary keys : ', student.keys())

# To see all the values in the dictionary, we use values() method
print('Dictionary values : ', student.values())

# To see all the key-value pairs in the dictionary, we use the items() method
print('Dictionary items : ', student.items())

# We can iterate over the key and value of the dictioanry simultaneously using the items() method
for key,value in student.items():
    print(key,' : ',value)




