#!/usr/bin/env python3

# Author: Mitch Gregoris
# Author ID: 133349191
# Date Created: 2023-10-12

# Return Text Value Function
def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name 
    return greeting


# Return Number Value Function
def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

    
#Main Program
if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))

# def hello():
#     print('Hello World')
#     print('Inside a Function')

# my_stuff = hello()
# print('Stuff return from hello():',my_stuff)
# print('the object my_stuff is of type:',type(my_stuff))




number = return_number_value()
print(number)
print(number + 5)
print(return_number_value() + 10)

# number = return_number_value()
# print('my number is ' + str(number))