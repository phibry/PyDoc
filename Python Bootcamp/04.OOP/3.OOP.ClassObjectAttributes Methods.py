

class Dog():
    # Class object Attribute: Are the same for every instance of a class
    # no self Keyword, than self refers to the instance not the object
    species = 'mammal'  # all dogs are mammals

    def __init__(self, breed, name):

        self.breed = breed
        self.name = name

    # Methods are functions inside a class.
    # Used to perform operations that utelize the defined attribute

    # OPERATIONS/Actions --> Methods
    def bark(self, number):  # with self it connects to the instance
        print('Woof! My name is {} and the number is {}'.format(self.name, number))


my_dog = Dog('Retriever', 'Alba')
your_dog = Dog('Lab', 'Chris')
print(my_dog.species)
my_dog.bark(50)  # Method called with ()
your_dog.bark(10)  # the number is not self: -> only this method want it.


class Circle():
    # Class Object Attribute
    # True for every instance of this class
    pi = 3.14  # pi is always 3.14

    def __init__(self, radius=1):
        self.radius = radius

    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2

    def get_area(self):
        return self.radius**2 * Circle.pi


my_circ = Circle()
print(my_circ.pi)
print(my_circ.radius)
print(my_circ.get_circumference())

my_newcirc = Circle(30)
print(my_newcirc.get_circumference())
print(my_newcirc.get_area())
