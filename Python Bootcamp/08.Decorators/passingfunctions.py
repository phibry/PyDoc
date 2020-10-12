# def func():
#     return 1


# print(func())
# print(func)


# def hello():
#     return 'Hello!'


# print(hello())

# # Reassigning the function
# greet = hello
# print(greet())
# del hello
# # print(hello())

# # Still works after deleting the hello function
# print(greet())


###
###
###

# def hello(name='Jose'):
#     print('The hello() function has been executed!')

#     # function inside a function
#     def greet():
#         return '\t This is the greet() func inside hello!'

#     def welcome():
#         return '\t This is welcome() inside hello!'

#     print("I am going to return a function!!")

#     if name == 'Jose':
#         return greet
#     else:
#         return welcome
#     # print(greet())
#     # print(welcome())
#     # print('This is the end of the hello function!')


# # hello()
# my_new_func = hello()
# my_new_func = hello('Jose')
# print(my_new_func())


# def cool():

#     def super_cool():
#         return 'I am very cool!'

#     return super_cool


# some_func = cool()
# print(some_func)
# print(some_func())


###
###
###
def hello():
    return 'Hi Jose!'


def other(some_def_func):
    # Passing a function as an argument
    print('Other code runs here!')
    print(some_def_func())


print(hello())
other(hello)
