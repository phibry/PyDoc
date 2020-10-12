# while some_boolean_condition:
#   do something
# else:
#   do smth different

x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('x is not less than 5')

'''
To add additional funcionality you can use:
break:      Breaks out of the current closest enclosing loops.
continue:   Goes to the top of the closest enclosing loop.
pass:       Doe nothing at all
'''
x = [1, 2, 3]
for item in x:
    # comment
    pass  # Do nothing at all: Placeholder for avoiding an error
print('end of my scipt')


mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue  # Goes back to the top and continues with the loop
    print(letter)


for letter in mystring:
    if letter == 'a':
        break  # Breaks the loop
    print(letter)


x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
