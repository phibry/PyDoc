# Problem 1
# Handle the exception thrown by the code below by using try and except blocks

# try:
#     for i in ['a', 'b', 'c']:
#         print(i**2)
# except TypeError:
#     print('Wrong data type!')


# Problem 2
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
x = 5
y = 0

z = x / y

try:
    z = x / y
except ZeroDivisionError:
    print('You tried to divide through 0!')
finally:
    print('Try again')


# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
# def ask():
#     while True:
#         try:
#             userinput = (int(input('Integer: ')))
#         except Exception:
#             print('Something went wrong!')
#             continue
#         else:
#             print(f'Thanks for your input: {userinput**2}')
#             break
#     print(f'Thanks for your input: {userinput**2}')


# ask()
