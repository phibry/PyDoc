# Find e to the Nth Digit
# Just like the previous problem, but with e instead of π (pi). Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.
import math


def calce(dig):
    return round(math.e, dig)


roundTo = input(
    'Enter the number of digits you want after the decimal for e: ')
try:
    roundint = int(roundTo)
    print(calce(roundint))

except:
    print('You did not enter an integer')
