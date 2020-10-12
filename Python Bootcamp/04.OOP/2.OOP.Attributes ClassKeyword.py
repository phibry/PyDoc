mylist = [1, 2, 3]
# mylist.append()  # alot of functions

myset = set()
# myset.add()
type(myset)  # -> set

# With a close you can define your own objects


class Dog():  # Create a sample class with they keyword class

    # init-method. Constructor for a class: Get called automaticly
    # self connects this method to this instance of the clas
    # allows to refer to itself
    def __init__(self, breed, name, spots):
        # Attributes
        # We take in the argument
        # assign it using self.attribute_name

        # Expect string
        self.breed = breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots


my_dog = Dog('Retriever', 'Alba', False)  # instance of sample
print(type(my_dog))
print(my_dog.__dict__)
