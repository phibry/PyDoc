t = (1, 2, 3)
# print(t[0])

from collections import namedtuple

Dog = namedtuple("Dog", "age breed name")
sam = Dog(age=2, breed="Lab", name="Sammy")
print(sam)
print(sam.age)
print(sam[0])  # index of age


Cat = namedtuple("Cat", "fur claws name")
c = Cat(fur="Fuzzy", claws=False, name="Kitty")
print(c)
print(c.name)
