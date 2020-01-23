# def add_tow(a,b):
#     return a + b
# total = add_tow(5,5)
# print(total)
# # print(add_tow(5,6))
# #! user input
# def add_tow(num1,num2):
#     return num1 + num2
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(add_tow(a,b))
#! string by function
#todo: the same function can be use for string
# a = input("Enter first name: ")
# b = input("Enter second name: ")
# print(add_tow(a,b))
#! print vs return
# def function(a,b,c):
#     return a+b+c #todo: its batter way
# total = function(5,6,7)
# print(total)
#! .....
# def function(num1,num2,num3):
#     print(num1+num2+num3)
# function(7,8,9)
#! function practice
# def name(num):
#     return num[-1]
# print(name("akash"))
#! odd even by function
# def odd_even(number):
#     if number % 2 == 0:
#         return "The number is even"
#     else:
#         return "The number is odd"
# print(odd_even(9))
#!.....same code but its batter
# def odd_even(number):
#     if number % 2 == 0:
#         return "The number is even"
#     return "The number is odd"
# print(odd_even(9))
#! boolian true false
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     return False
# print(is_even(11))
#!...... its can be make more shortcut
# def is_even(num):
#     return num%2 == 0
# print(is_even(10))
#! without pass parametar in function
# def func():
#     return "This is holiday"
# print(func())
#! grater 3 number
#todo: its some complex type
# def grater(a,b,c):
#     if a > b:
#         return a
#     elif b > c:
#         return b
#     return c
# print(grater(10,15,5))
#! ....easy way for under stand
# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     return c
# print(greatest(10,15,10))
#! function inside function
# def grater(a,b):
#     if a>b:
#         return a
#     return b

# def greatest(a,b,c):
#     # bigger = grater(a,b)
#     # return grater(bigger,c)
#     #! or its more complex
#     return grater(grater(a,b),c)
# print(greatest(50,10,20))
#! function return with two value
# def func(num1,num2):
#     total = num1 + num2
#     multi = num1 * num2
#     return total,multi

# total,multi = func(5,6)
# print(total)
# print(multi)
