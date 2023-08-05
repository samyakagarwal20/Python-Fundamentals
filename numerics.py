"""
-----------------------------------------------------------------------------------------------------------
Arithmetic operators
-----------------------------------------------------------------------------------------------------------
"""
# The following are the different arithmentic operators: +, -, *, division (/), floor division (//), exponent (**), modulus (%)
print('Division operation', 3 / 2)
print('Floor Division operation', 3 // 2)
print('Exponent operation', 3 ** 2)
print('Modulus operation', 3 % 2)

# The order of execution of the operations is similar to that of other lanaguages like Java 

# The following are the shorthand-operators : +=, -=, etc.
num = 1
num += 1
print('Result after shorthand oeprator += : ', num)


"""
-----------------------------------------------------------------------------------------------------------
Logical operators
-----------------------------------------------------------------------------------------------------------
"""
# The following are the comparision operators which returns a boolean value: ==, !=, <, >, <=, >=
num_1 = 3
num_2 = 2
print('Result of 3 > 2 : ', num_1 > num_2)
print('Result of 3 == 2 : ', num_1 == num_2)
print('Result of 3 != 2 : ', num_1 != num_2)
print('Result of 3 >= 2 : ', num_1 >= num_2)


"""
-----------------------------------------------------------------------------------------------------------
Type Casting
-----------------------------------------------------------------------------------------------------------
"""
# It refers to the conversion of datatype of a variable
# It can be used for converting numeric data in string format to number
num_1 = '100'
num_2 = '200'
print('Result of ("100" + "200") without casting : ', num_1 + num_2)
num_1 = int(num_1)          # converting string to int
num_2 = float(num_2)        # converting string to float
print('Result of ("100" + "200") with casting : ', num_1 + num_2)


"""
-----------------------------------------------------------------------------------------------------------
Numeric Data related methods
-----------------------------------------------------------------------------------------------------------
"""

# to find the absolute value of, use abs() method
print('Absolute value of -3 : ', abs(-3))

# to round up any value to the nearest integer, use round() method
# it takes 2 arguments - the value and the no. of places the value has to be rounded off
print('Round off value for 3.75 :', round(3.75))
print('Round off value for 3.75 till 1 places after the decimal : ', round(3.75,1))
