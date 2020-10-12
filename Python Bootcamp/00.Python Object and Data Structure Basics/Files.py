# I/O Basic Files in Python
myfile = open('myfile.txt')
# myfile = open('whoops_wrong.txt') # wrong name

myfile = open('myfile.txt')
myfile.read()
>> > myfile = open('C:/Users/phili/OneDrive/Udemy/Python Bootcamp/myfile.txt')
>> > myfile.read()
'Hello this is a text file\nthis is the second line\nthis is the third line\n'

>> > myfile.read()
''
# read doens't work anymore: Imagine the curser is at the end of the file, reset it
>> > myfile.seek(0)
0
>> > myfile.read()
'Hello this is a text file\nthis is the second line\nthis is the third line\n'

>> > myfile.seek(0)
0
>> > myfile.readlines()
['Hello this is a text file\n', 'this is the second line\n', 'this is the third line\n']

# File Location
>> > myfile = open('C:\\Users\\phili\\OneDrive\\Udemy\\Python Bootcamp\\myfile.txt')
>> > myfile = open('C:/Users/phili/OneDrive/Udemy/Python Bootcamp/myfile.txt')

>> > myfile.close()  # u have to close it

# Best Practices
with open('C:\\Users\\phili\\OneDrive\\Udemy\\Python Bootcamp\\myfile.txt') as mnewfile:
...     content = mnewfile.read()

with open('myfile.txt', mode='r') as myfile:
    contents = myfile.read()
# mode = 'r' -> read
# mode = 'w' -> write only (overwrite), or create a new file
# mode = 'a' -> append
# mode = 'r+' -> reading and writing
# mode = 'w+' -> writing and reading (overwrite), or create a new file
print(contents)

with open('my_new_file.txt', mode='r') as f:
    print(f.read())

with open('my_new_file.txt', mode='a') as f:
    f.write('\nFOUR ON FOURTH')

with open('my_new_file.txt', mode='r') as f:
    print(f.read())


with open('asdasd.txt', mode='w') as f:
    f.write('I CREATED THIS FILE!')

x = open('test.txt', 'w')
x.write('Hello World')
x.close()
