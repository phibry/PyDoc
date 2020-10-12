print('a'.islower())

b = 'hello'
print(len(b))

mynums = [1, 2, 3, -4]
test = list(map(lambda num: num * num, mynums))
print(test)

celsius = [0, 10, 20, 34.5]  # degree celsius

fahrenheit = [((9 / 5) * temp + 32) for temp in celsius]
print(fahrenheit)


import string

print(string.ascii_lowercase)


a = 'Hello World'
print(a)
print(a.replace(" ", "").lower())
