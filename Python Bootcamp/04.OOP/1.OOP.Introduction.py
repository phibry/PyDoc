# Object Oriented Programming allows programmer to create their own objects
# that have methods and attributes.

# Reacll that after defining a string, list, dictionary, or other objects,
# you were able to call methods off of them with .method_name() syntax

# These methods act as functions taht use
# information about the object, as well as the
# object itself to return results, or change the
# current object.

# For example this includes appending to a list,
# or counting the occurences of an element in
# a tuple.

# tuple OOP allows userts to create their own objects.

# The general format is often confusing when
# first encountered, and its usefuleness may not
# be completely clear at first.

# In general, OOP allows us to create code that
# is repeatable and organized.

# For much larger scipts of Python code,
# function by themselves aren't enough for
# organization and repeatability.

# Commonly repeated tasks and objects can be
# defined with OOP to create code that is more
# useable.

# Let's check out the syntax


# Defining a class: Normaly first letter is capitalized
class NameOfClass():

    # looks like a function but is a method in a class
    # this is a special init-method
    # it creates an instance the actual objects
    
    # -> self (instance itself) and the parameters of the instance
    def __init__(self, param1, param2):
        # pass a parameter and connect the parameter to an object itself, with self.
        self.param1 = param1
        self.param2 = param2

    # other method call
    # method that is connected to a class -> self
    # so it knows you are referring to this class.
    def some_method(self):
        # perform some action
        print(f'{self.param1} {self.param2}')



inst1 = NameOfClass('Philippo', 'Rieser')
inst1.some_method()
