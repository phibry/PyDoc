# Special Methods: Magic/Dunder
mylist = [1, 2, 3]
# print(len(mylist))


class Sample():
    pass


mysample = Sample()
# print(len(mysample))  # Error
# print(mysample)

# So how can I use in-built function on a my own user defined objects.
# -> Special Methods: Magic/Dunder -> douple underline __fun__


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}."

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')


b = Book('Python rocks', 'Phili', 200)
print(b)  # needs __str__ for printing the object
# print(len(b))

# del b
# print(b)

# del b  # delets b in the memory of the computer
# print(b)
print(b)
