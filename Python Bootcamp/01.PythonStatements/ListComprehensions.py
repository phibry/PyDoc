# Quickly creating lists in python.
mystring = 'hello'

# standard list
mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)


'''List Comprehension'''
mylist = [letter for letter in mystring]
print(mylist)

mylist = [x for x in 'word']
print(mylist)

mylist = [num for num in range(0, 11)]
print(mylist)

# Square of every number
mylist = [num**2 for num in range(0, 11)]
print(mylist)

# If statement: only even numbers
mylist = [x for x in range(0, 11) if x % 2 == 0]
print(mylist)

# Square of the even numbers
mylist = [x**2 for x in range(0, 11) if x % 2 == 0]
print(mylist)

celsius = [0, 10, 20, 34.5]  # degree celsius

fahrenheit = [((9 / 5) * temp + 32) for temp in celsius]
print(fahrenheit)


# If, else is possible. But readbility and replicateability are important for Python
result = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(result)


# Nested Loop
mylist = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        mylist.append(x * y)

print(mylist)

# Nested Comprehension List
mylist = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(mylist)
