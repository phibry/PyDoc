# Problem 1
# Create a generator that generates the squares of numbers up to some number N.


def gensquares(N):
    for x in range(N):
        yield x**2


# for x in gensquares(10):
    # print(x)


# Problem 2
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library. For example:

import random

random.randint(1, 10)


def rand_num(low, high, n):
    for x in range(n):
        yield random.randint(low, high)


# for num in rand_num(1, 10, 12):
#     print(num)

# Problem 3
# Use the iter() function to convert the string below into an iterator:
s = 'hello'
# code here
s_iter = iter(s)
# print(next(s_iter))
# print(next(s_iter))
# print(next(s_iter))

# Extra Credit!
# Can you explain what gencomp is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)
my_list = [1, 2, 3, 4, 5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
print(list(gencomp))
