# Errors are bound to happen in cour code!
# Especially when someone else ends up using it in an unexpected way.
# We can use error handling to attempt to plan for possible errors.

# For example, a user may try to write to a file that was only opened in mode='r'
# Currently of there is any type of error in your code, the entire script will stop.
# We can use Error Handling to let the script continue with other code, even if there is an error.

# try:      This is the block of code to be attempted (may lead to an error)
# except:   Block of code will execute in case there is an error in try block
# finally:  A final blcok of code to be executed, regargless of an error.


# def add(n1, n2):
#     print(n1 + n2)


# add(10, 20)

# number1 = 10
# number2 = input("Please provide a number: ")  # won't work: is a string

# add(number1, number2)
# everything after this line, won't be executed

try:
    # Want to attempt this code
    # May have an error
    # result = 10 + 10
    result = 10 + '10'
except TypeError:
    print("Hey it looks like you aren't adding correctly!")
else:
    print('Add went well!')
    print(result)

# print(10 + '10')
