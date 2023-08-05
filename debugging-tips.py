# We can check the methods availaable for a particular variable by using the dir() method
message = 'hello world'
print(dir(message))
      
# To get the help regarding any class, we can use the help() method
print(help(str))

# We can also search for a specific method of a class
print(help(str.find))

# We can check the datatype of any variable using the type() method
num = 3
print('datatype of 3 : ', type(num))
num = 3.14
print('datatype of 3.14 : ', type(num))