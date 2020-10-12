from collections import Counter

l = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
print(Counter(l))

s = "aaaaassasasvvavasvbbabsbabb"
print(Counter(s))

string = "How many times does each word show up in this sentence word word show up up"
words = string.split()
print(Counter(words))

# Methods of Counter
c = Counter(words)
print(c.most_common(3))

# sum(c.values())  # total of all counts
# c.clear()  # reset alls counts
# list(c)  # list unique elements
# set(c)  # convert to a set
# dict(c)  # convert to a regular dictionary
# c.items()  # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))  # convert from a list of (elem, cnt) pairs
# c.most_common()[: -n - 1 : -1]  # n least common elements
# c += Counter()  # remove zero and negative counts
