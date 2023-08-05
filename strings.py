# Printing directly to console
print('Hello world')

# Printing via variable
message = 'this line is printed via variable'
print(message)

# String can be represented using '<text>', "<text>" and """<text>""" or '''<text>'''
# Printing via multi-line string """<text>""" or '''<text>'''
message = ''' 
    This is a multi-line string :-
    (1) This is line 1
    (2) This is line 2
    '''
print(message)

# Fetching the length of string
message = 'Hello world'
print('Length of "Hello world" : ',len(message))

# Fetching a specific character from the string
print('Fetching characters at index 0 and 6 from start of string : ',message[0], message[6])


# All the operations which involves fetching the string based on startIdx and endIdx falls under the concept of Slicing
# Fetching a sequence of characters from string
# In message[0:5], startIdx = 0 and endIdx = 5, the result is in the range [start,end) ,i.e., start is inclusive but end is not
print('Fetching a sequence of characters in range [0,5) : ', message[0:5])

# By default. the value of startIdx = 0, thus, even if we don't specify its value, we get the same result
print('Fetching sequence of characters upto index 5 in the range [0,5) : ',message[:5])

# If we specify only the startIdx and not the endIdx, then the result will be in the range [startIdx, length of string)
print('Fetching sequence of characters from startIdx 6 till end of string', message[6:])

"""
-----------------------------------------------------------------------------------------------------------
String Methods
-----------------------------------------------------------------------------------------------------------
"""

# Converting the entire string to lowercase
print('Printing the string in lowercase : ', message.lower())

# Converting the entire string to uppercase
print('Printing the string in ippercase : ', message.upper())

# To count the frequency of a single or a sequence of characters in the string
print('Fetching the frequency of "l" : ', message.count('l'))
print('Fetching the frequency of "Hello" : ', message.count('Hello'))

# To fetch the first index where a single or sequence of characters occur in the string, we use find()
print('Fetching the starting index of "l" : ',message.find('l'))
print('Fetching the starting index of "world" : ',message.find('world'))

# If we try to find the startIdx of any character(s) which doesn't exists in the string, then the result is -1
print('Fetching the starting index of "india" : ', message.find('india'))

# We can replace a character or a sequence of characters in a string with some new string using replace(old_string, new_string)
# The replace() doesn't makes the changes in-place instead it returns a new string entirely
new_message = message.replace('world','universe')       # instead of creating a new variable we can directly assign the modified value to the previous string as well
print('String before replace() : ', message)
print('String after replace("world","universe") : ', new_message)

# Concatenation of strings
print('"Hello" + "Peter" : ', 'Hello' + ', Peter')        # using + operator
print('Concatenation using f-strings : ', '{}, {}'.format('Hello','Peter'))     # using format() method where we supply the values for placeholders

# f-strings provides more readability as we can directly specify the variables inside the placeholders
greeting = 'Hello'
person = 'Peter'
print('String formatting using f-strings : ', f'{greeting}, {person.upper()}')


