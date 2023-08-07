nums = [1,2,3,4,5]

# iterating over list
print('--------------------------------')
for num in nums:
    print(num)
print('--------------------------------')


# iteration with break
print('--------------------------------')
print('Iteration with break')
for num in nums:
    if num == 3:
        print('Found 3 !')
        break
    print(num)
print('--------------------------------')


# iteration with continue
print('--------------------------------')
print('Iteration with continue')
for num in nums:
    if num == 3:
        print('Skipping 3 !')
        continue
    print(num)
print('--------------------------------')


# iteration with nested loop
print('--------------------------------')
print('Nested loops')
for num in nums:
    for letter in 'abc':
        print(num,letter)
print('--------------------------------')

# iteration with range()
# by default, it starts from 0
print('--------------------------------')
print('Iteration with range()')
for num in range(10):
    print(num)
print('--------------------------------')

# iteration with range(start,end)
print('--------------------------------')
print('Iteration with range(start,end)')
for num in range(1,11):
    print(num)
print('--------------------------------')

# The for loops iterates for a certain number of values which means that the number of iterations are known beforhand
# But, the while loop iterates until a certain condition is met, i.e., the number of iterations are not known in advance

# iteration with while loop
print('--------------------------------')
print('Iteration with while loop')
x = 0
while x < 10:
    if(x == 5):
        print('Skipping 5')
        x += 1
        continue
    print(x)
    x += 1
print('--------------------------------')
