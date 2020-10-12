# def name_of_function(name):
#   '''
#   Docstring explains function.
#   '''
#   print('Hello' + name)

# name_of_funtion('Jose') -> Prints: Hello Jose


def name_function():
    '''
    DOCSTRING: Information about the function
    Input: no input
    Output: Hello
    '''
    print('Hello')


help(name_function)
name_function()


def say_hello(name='NAME'):
    # print('Hello ' + name)
    return 'Hello ' + name


# say_hello()  # Default is NAME
# say_hello('Tanja')

result = say_hello('Philipp')
print(result)


def add(n1, n2):
    return n1 + n2


res = add(10, 20)
print(res)


# Find our if the word "dog" is in a string?
def dog_check(mystring):
    # if 'dog' in mystring.lower():  # is actually a boolean, no need for if statement
    #     return True
    # else:
    #     return False
    return 'dog' in mystring.lower()


print('dog' in 'dog ran away')


print(dog_check('My dog ran away'))
print(dog_check('My cat ran away'))
print(dog_check('My Dog ran away'))


# Pig Latin
def pig_latin(word):

    first_letter = word[0]
    # Check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word


print(pig_latin('apple'))
