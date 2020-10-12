# variable names get stored in name space. variable names have a scope

# errors like: this variable is not defined. Why this happens and how to fix?

x = 25  # assigns out of function:


def printer():
    x = 50
    return x


print(x)  # doesnt affect function
print(printer())

# LEGB Rule:
# L: Local - Names assigned in any way within a function (def or lambda),
#            not declared global in that function.
# E: Enclosing function locals - Names in the local scope of any and all
#            enclosing function (def or lambda), from innter to outer.
# G: Global (module) - Names assigned at the top-level of a module file,
#            or declared global in a def within the file.
# B: Built-In (Python) - Names preassigned in the built-in names module:
#            open, range, SyntaxError,...


# L:
# lambda num:num**2

# E:
name = 'IM A GLOBAL'  # Global


def greet():
    # Enclosing

    name = 'Sammy'
    # Comment name
    # 3.G: Look globally: Yes outside it is assigned.

    def hello():
        # Local
        # 1.L: Do i have name assigned here? -> No
        # 2.E: Do i have name assigned in the scop of enclosing function (greet) -> yes
        name = 'IM A LOCAL'
        print('Hello ' + name)

    hello()


greet()

# G:
help(len)  # Then it is a built-int function


#
#
#
#
x = 50


def func(x):
    # Declare a global x: Go to a namespace and grab the global x
    # global x # Don't do that: Use a return for a new assignment
    print(f'X is {x}')

    # Local Reassignment ON a GLOBAL Variable!
    x = 200
    print(f'I JUST LOCALLY CHANGED GLOBAL X to {x}')
    return x


# func(x)
# print(x)  # still 50. Reassignment only happens inside the enclosing function

# print(x)
# func()

x = func(x)
print(x)
