#!/usr/bin/env python3

# Author: Mitch Gregoris
# Author ID: 133349191
# Date Created: 2023-10-12

def operate(number1, number2, operator):
    # Place logic in this function
    if operator == 'add':
        sum = number1 + number2
    elif operator == 'subtract':
        sum = number1 - number2
    elif operator == 'multiply':
        sum = number1 * number2
    #elif operator == "divide":
     #   sum = number1 / number2
    elif (operator != 'add') or (operator != 'subtract') or (operator != 'multiply') or (operator != 'divide'):
        sum = str('Error: function operator can be "add", "subtract", or "multiply"')
        print(sum)
    return sum
    
if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))