# Inheritance is basically defining a new class with the help of class that already have been defined


# class Animal():  # Base Class
#     def __init__(self):
#         print("Animal created")

#     def who_am_i(self):
#         print('I am an animal')

#     def eat(self):
#         print('I am eating')


# class Dog(Animal):  # inherit the base Class Animal
#     def __init__(self):
#         # creating an instance of animal, while creating an instance of dog
#         Animal.__init__(self)
#         print("Dog created")

#     def who_am_i(self):  # recreated this method for Dog Class
#         print('I am a dog!')

#     def bark(self):  # add a new method only dog dog-class
#         print('Woof!')


# an1 = Animal()
# an1.eat()
# an1.who_am_i()

# dog1 = Dog()
# dog1
# dog1.eat()
# dog1.who_am_i()


'''Polymorphism: optional'''
# Refers to the way in which different object classes can share the same name
# And those methods can be called from the same place even tho a vareity of
# different objects might be passed in


# class Dog():

#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return self.name + 'Says woof!'


# class Cat():

#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return self.name + 'Says meow!'


# niko = Dog('niko')
# felix = Cat('felix')

# print(niko.speak())
# print(felix.speak())

# for pet in [niko, felix]:
#     print(type(pet))
#     print(type(pet.speak()))
# # Both classes share the same method name of speak. but the type is different


# def pet_speak(pet):
#     print(pet.speak())


# pet_speak(niko)
# pet_speak(felix)


'''Abstract Classe: Only Base Class'''


class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError(
            'Subclass must implement this abstract method')
# Animal is only the base class for Subclasse
# We don't want to build an instance for it.


myanimal = Animal('fred')
# myanimal.speak()
# It is expected to inherit the class in a subclass


class Dog(Animal):

    def speak(self):
        return self.name + 'say wood!'


class Cat(Animal):

    def speak(self):
        return self.name + 'say meow!'


fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())


# An example would be opening files
# There are many different filetypes like: json, csv, txt, etc.
# U want to share the same method-name for all of them -> like dot_open()
