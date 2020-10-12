with open('my_new_file.txt', mode = 'r') as f:
    print(f.read())

with open('my_new_file.txt', mode = 'a') as f:
    f.write('\nFOUR ON FOURTH')

with open('my_new_file.txt', mode = 'r') as f:
    print(f.read())


with open('asdasd.txt', mode = 'w') as f:
    f.write('I CREATED THIS FILE!')
