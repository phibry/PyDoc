# Find PI to the Nth Digit
# Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.
import math


def calcpi(dig):
    return round(math.pi, dig)


roundTo = input(
    'Enter the number of digits you want after de decimal for Pi: ')
try:
    roundint = int(roundTo)
    print(calcpi(roundint))

except:
    print('You dif not enter an integer')
