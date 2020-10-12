# my_iterable = [1,2,3]
# for item_name in my_iterable:
#   print(item_name)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in mylist:
#     print(num)

# for num in mylist:
#     # Check for even
#     if num % 2 == 0:
#         print(num)
#     else:
#         print(f'Odd Number {num}')


# list_sum = 0

# for num in mylist:
#     list_sum = list_sum + num
#     # print(list_sum)

# print(list_sum)


# mystring = 'Hello World'

# for letter in mystring:
#     print(letter)


tup = (1, 2, 3)
for item in tup:
    print(item)


mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
# Tuple-Pairs -> 4 items in mylist
for item in mylist:
    print(item)

'''Tuple unpacking'''
for a, b in mylist:
    print(a)
    print(b)


mylist = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in mylist:
    print(b)


'''Looping through a dictionarie'''
d = {'k1': 1, 'k2': 2, 'k3': 3}
for key, value in d.items():
    print(value)

for value in d.values():
    print(value)

for key in d.keys():
    print(key)
