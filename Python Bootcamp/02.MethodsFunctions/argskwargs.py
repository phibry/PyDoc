# *args     arguments
# **kwargs  keyword arguments


# a and b are positional arguemnts
# a = 40
# b = 60
def myfunc(a, b):
    # Returns 5% of the sum of a and b
    return sum((a, b)) * 0.05


print(myfunc(40, 60))


# What if we cant to work with more parameters?
def myfunc(a, b, c=0, d=0):
    # Returns 5% of the sum of a and b
    return sum((a, b, c, d)) * 0.05


print(myfunc(40, 60))
print(myfunc(40, 60, 20))
print(myfunc(40, 60, 1000))


# *args
# treat args a tuple of arguments
def myfunc(*args):
    return sum(args) * 0.05


print(myfunc(40, 60))
print(myfunc(40, 60, 100, 1, 34, 50, 60))


# **kwargs
# dictionarie of keyword arguments
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        # print(f'My fruit of choice is {kwargs['fruit']}')
        print('My fruit of chocie is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


myfunc(fruit='apple', veggie='lettuce')


# *args and **kwargs
def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f'I would like {args[0]} {kwargs["food"]}')
    print('I would like {} {}'.format(args[0], kwargs['food']))


myfunc(10, 20, 30, fruit='orange', food='eggs', animal='dog')


def myfunc(*args):
    arglist = []
    for a in args:
        if a % 2 == 0:
            arglist.append(a)
    return arglist


print(myfunc(1, 2, 3, 4, 5, 6))
c = 'c'
c = c.upper()
print('a' + 'b' + c)


def myfunc(string):
    mylist = [letter for letter in string]
    b = ""
    for index, a in enumerate(mylist):
        # starts with 0
        if index % 2 == 0:
            b += a.lower()
        else:
            b += a.upper()
    return b


print(myfunc('Anthropomorphism'))


print(1, 2, 3, 4)
