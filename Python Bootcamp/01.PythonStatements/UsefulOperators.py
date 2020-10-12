# mylist = [1, 2, 3]
# for num in range(1, 10, 3):
#     print(num)

# # range is a generator
# print(range(1, 10, 3))
# print(list(range(1, 10, 3)))

# index_count = 0

# for letter in 'abcde':
#     print(f'At index {index_count} the letter is {letter}')
#     index_count += 1


# index_count = 0
# word = 'abcde'

# for letter in word:
#     print(word[index_count])
#     index_count += 1

# '''enumerate'''
# word = 'abcde'
# for item in enumerate(word):
#     print(item)

word = 'abcde'
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')


# '''zip, zipps together lists'''
# mylist1 = [1, 2, 3, 4, 5, 6]
# mylist2 = ['a', 'b', 'c']
# mylist3 = [100, 200, 300]

# print(zip(mylist1, mylist2, mylist3))
# for item in zip(mylist1, mylist2, mylist3):
#     print(item)

# print(list(zip(mylist1, mylist2)))

# # unpack
# for a, b, c, in zip(mylist1, mylist2, mylist3):
#     print(a)
#     print(b)
#     print(c)


# '''in'''
# print('x' in [1, 2, 3])
# print('x' in ['x', 'y', 'z'])
# print('a' in 'a world')

# d = {'mykey': 345}
# print('mykey' in d)
# print(345 in d.keys())
# print(345 in d.values())


# '''math'''
# mylist = [10, 20, 30, 40, 100]
# print(min(mylist))
# print(max(mylist))


'''random library'''
# from random import shuffle
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(mylist)
# shuffle(mylist)
# print(mylist)
# shuffle(mylist)
# print(mylist)

# '''random integer'''
# from random import randint
# print(randint(0, 100))
# mynum = randint(0, 100)
# print(mynum)


'''input'''
# input('Enter a number here: ')

# result = input('What is your name? ')
# print(result)
# result of an input is always a string
# int(intput('Transforms Input into an integer'))
