# __name__ and '__main__'
# An often confusing part of Python is a mysterious line of code:
#      if __name__=='__main__':

# Sometime when you are importing from a module, you woulk like to know
# whether a modules function is being used as an import, or if you are
# using the original .py file of that module

# If you run a code in cmd. Every line of code with an indent level of 0
# will gets run.
# print('hello')
# def ...():
# class ...():


def myfunc():
    print('Hello')


# in Python is an inbuilt function called __name__ <- BUILT int variable
# __name__ gets assigned a string while running a file
# If you run smth directly in python
# __name__ gets assigned to a string '__main__'
# __name__ = '__main__'
# and it checks if true
if __name__ == '__main__':
    myfunc()
