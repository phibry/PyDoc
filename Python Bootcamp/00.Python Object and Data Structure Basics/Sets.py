# Sets: unordered collections of unique elements
myset = set()
myset.add(1)
myset.add(2)
myset.add(2)  # doenst add a 2nd 2

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]
set(mylist)  # {1, 2, 3}
