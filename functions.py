# functions are a block of statements which are used to perform a specific task
# We define a function using the def keyword
# In case, if we don't want to do anything with the function currently but might be interested in later modifying it, then we can use the pass keyword

def hello_func():
    pass

# returning the reference of the function
print('Reference of the function : ', hello_func)

# executing the function
# If we are not returning anything from the function then it returns 'None' as result
print('Executing the function : ', hello_func())

# In case if are defining the same implementation in multiple places and we are asked to change something in it, then we need to make changes in all those places. 
# Instead, it would be better to define the implementation in one place and references it. That's where the functions comes into picture
# This practice is how the DRY (Don't Repeat Yourself) principle is implemented
def hello_world_func():
    print('hello world')

hello_world_func()

# returning value from a function
def hello_world_func_2():
    return 'Hello World'

print('Value returned from hello_world_func_2 : ', hello_world_func_2().upper())

# function with parameters
def func_with_parameter(greeting):
    return f'{greeting} function'

print('Value returned from func_with_parameter() : ', func_with_parameter('Hello'))

# function with default parameter
def greeting_func(greeting, name = 'Peter'):
    return f'{greeting}, {name}'

print('Invoked greeting_func() with 1 argument : ', greeting_func('Thank You'))
print('Invoked greeting_func() with 2 argument : ', greeting_func('Thank You','Vegeta'))

# We can pass any number of positional arguments in a function using the *args parameter
def args_func(*args):
    print(args)

# We can pass any number of keyword arguments to a function using the **kwargs parameter
def kwargs_func(**kwargs):
    print(kwargs)

def args_kwargs_func(*args, **kwargs):
    print(args)
    print(kwargs)

# When passing all the positional arguments, they are represented in the form of a tuple
args_func('Tony',25,85000,'Male')

# When passing the keyword arguments, they are represented in the form of a dictionary
kwargs_func(name = 'Tony', age = 25, salary = 85000, gender = 'Male')

# We can unpack the values from a list and pass them to the function using the * operator as positional arguments
courses = ['AI','ML','Blockchain','DevOps','Cybersecurity']
student_data = {'name': 'Tony', 'age': 25, 'salary': 85000, 'gender': 'Male'}
args_kwargs_func(courses,student_data)          # noth of these arguments are considered as positional arguments
args_kwargs_func(*courses,**student_data)

# To mention as comments what a particular function do in terms of maintenance, we should provide a doc string in it
def doc_string_func():
    """This is a demo function to demo the doc string"""
    pass
