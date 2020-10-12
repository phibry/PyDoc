# def create_cubes(n):
#     result = []  # needed to store the list in memory
#     for x in range(n):
#         result.append(x**3)
#     return result


# # usefull if u want to have the entire list
# print(create_cubes(10))


# # needs only one value at a time
# for x in create_cubes(10):
#     print(x)


def create_cubes(n):
    for x in range(n):
        yield x**3


# with yield: memory efficient
# u don't have to save the entire cube list in memory
for x in create_cubes(10):
    print(x)

listc = list(create_cubes(10))  # if u want to have the list
print(listc)


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for x in gen_fibon(10):
    print(x)
