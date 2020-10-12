# one.py


def func():
    print('func() in one.py')


# def function():
#     pass


# def function2():
#     pass


print('Top level in one.py')

if __name__ == '__main__':
    # Run the script!
    # func()
    # function()
    # function2()
    print('one.py is being run directly!')
else:
    print('one.py has been imported!')
