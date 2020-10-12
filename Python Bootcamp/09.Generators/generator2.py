def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()
print(g)

print(next(g))
print(next(g))
print(next(g))
# print(next(g))
# the for in the for loops calls next() until the last element


s = 'hello'
for letter in s:
    print(letter)

# next(s)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
