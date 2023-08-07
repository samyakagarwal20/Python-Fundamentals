# Under conditionals, we deal with if-else, if-elif-else statements 
# the control flow is decided based on expressions which are evaluated to a boolean type
# The boolean type has only 2 values : True, False
# The following are some of the operators used in conditionals : and, or, not, all logical operators, is, etc

# The difference between == and is operator is that == checks if both the operands have the same values and are of the same type or not
# is operator check if both the operands refers to the object in memory

interest = 'AI'

if interest == 'Cloud':
    print('Interest is Cloud')
elif interest == 'Cybersecurity':
    print('Interest is Cybersecurity')
else:
    print('Interest is AI')

user = 'Peter Parker'
heroname = 'Spiderman'

if (user == 'Tony Stark' and heroname == 'Ironman'):
    print(f'user is {user} and heroname is {heroname}')
elif (user == 'Peter Parker' and heroname == 'Spiderman'):
    print(f'user is {user} and heroname is {heroname}')
elif (user == 'Gal Gadot' or user == 'Clark Kent'):
    print('heroes are from DC')

# Difference between == and is
a = [1,2,3,4]
b = [1,2,3,4]

print('a == b : ', a == b)
print('a is b : ', a is b)

# To further demonstrate, we will fetch the id for both the lists and compare them
print('Id of list a : ', id(a))
print('Id of list b : ', id(b))

# Thus, we can say that behind the scenes, (a is b) is evaluated as id(a) == id(b)

# The following are the different conditions which evaluates to False in python
# condition = False
# condition = None
condition = 0       # all numbers apart from 0 are evaluated as true
# condition = any empty sequence like '', [], ()
# condition = any empty mapping like {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluate to False')