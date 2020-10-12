# Quickly creata anonymous function. Used once and never referenced too.

'''Map: applies a function to everything in a list'''


def square(num):
    return num**2

my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

mappedlist = list(map(square, my_nums))
print(mappedlist)


def slicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']

print(list(map(slicer, names)))


'''filter: filter based of the condition of the function: must be boolean'''


def check_even(num):
    return num % 2 == 0

mynums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, mynums)))
for n in filter(check_even, mynums):
    print(n)


'''lambda expression'''


def square(num):
    result = num ** 2
    return result


print(square(3))
# turn this in a lambda function


def square(num):  # step 1
    return num ** 2


def square(num):
    return num ** 2  # step 2


lambda num: num ** 2  # step 3

# with map
test = list(map(lambda num: num ** 2, mynums))
print(test)

# with filter
test2 = list(filter(lambda num: num % 2 == 0, mynums))
print(test2)

# names
print(names)
print(list(map(lambda x: x[0], names)))
print(list(map(lambda x: x[::-1], names)))
