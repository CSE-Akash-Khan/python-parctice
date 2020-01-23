#!factorial use loop
#! 5 = 5*4*3*2
# user = int(input("Enter a number: "))
# number = user
# while user > 1:
#     user -= 1
#     number *= user
# if user == 0:
#     print(1)
# else:
#     print(number)
#! factorial use recursive
#! 5*4*3*2*1*1
# def factorial(n):
#     if n == 0:
#         return 0
#     else:
#         return n*factorial(n-1)
# user = int(input("Enter a number: "))
# print(factorial(user))
#! fibonacci serice
#todo: 0 1 1 2 3 5 8 13---------->
# def fibonacci_seq(user):
#     a = 0
#     b = 1
#     if user == 1:
#         print(a)
#     elif user == 2:
#         print(a, b)
#     else:
#         print(a,b, end = " ")
#         for i in range(user-2):
#             c = a + b
#             a = b
#             b = c
#             print(b, end = " ")
# user = int(input("Enter a number: "))
# fibonacci_seq(user)

#! leap year
# user = int(input("Enter a year: "))
# if user % 4 == 0:
#     print("This year is leap year")
# else: 
#     print("This year is not leap year")
#! prower x y
# z = int(input("Enter base: "))
# x = int(input("Enter power: "))
# y = int(input("Enter more power: "))
# # power = x**y
# d = pow(x,y)
# # print(d)
# power = pow(z,d)
# print(power)
#! sum of number
#todo: 256 = 2+5+6 = 13
# user = input("Enter sum of number: ")
# total = 0
# for i in user:
#     var = int(i)
#     total += var
# print(total)
#todo: this same program in c concept
# user = int(input("Enter sum of number: "))
# temp = user
# sumation = 0
# while temp != 0:
#     r = temp % 10
#     sumation += r
#     temp = temp//10
# print(sumation)
#! armestrong number print
#todo: 256 = 2**3 + 5**3 + 6**3
# user = input("Enter sum of number: ")
#todo: this is not possible becouse input always take string and total give int type
# total = 0
# for i in range(len(user)):
#     # n = len(user)
#     var = int(user[i])
#     total += var**3
# if total == user:
#     print("yes",total)
#! try another way
# a = int(input("Enter sum of number: "))
# b = str(a)
# p = len(b)
# user = a
# total = 0
# while user != 0:
#     r = user % 10
#     total =total+ pow(r,p)
#     user = user // 10
# if total == a:
#     print("This number is an armestrong ")
# else:
#     print("This number is not armestrong ")

#! plindrome
#todo: noyon reverse korleoo noyon ii hobe
# users = input("Enter sum character: ")
# user = users.upper()
# if user == user[::-1]:
#     print("this is plain droom")
# else:
#     print("This is not plain droom")
# user = int(input)
#todo: its make by c concept
# user = int(input("Enter sum of number: "))
# temp = user
# total = 0
# while temp != 0:
#     r = temp % 10
#     total = (total*10) + r
#     # total *= 10 + r
#     temp = temp // 10
# if total == user:
#     print("This number is a plindrome")
# else:
#     print("This number in not plindrome")
#? coaching home work
#! 1 number
# for i in range(1,101):
#     print(i**2)
#! 6 number 
#todo same :it has use inner loop
# total = 0
# for i in range(1,2):
#     for j in range(23,46,11):
#         total += i**j
#         i += 1
#         print(total)
#! problem 6
#todo same :but its easy
# total = 0
# j = 1
# for i in range(23,46,11):  
#     total += j**i
#     j += 1
#     print(total)
# # print(total)
#! problem 3
#todo: 1 + 3**3 + 5**5 + 7**7
# user = int(input("Enter number: "))
# j = 1
# for i in range(1,user,2):
#     total = i**j
#     j+=2
#     print(total)
#!problem 2
#todo: 1 + 1/2 + 1/3 + 1/4..........1/n
# user = int(input("Enter a number: "))
# j = 1
# for i in range(1,user+1):
#     total = j/i
#     print(total)
#! probelm 5
#todo: 1 + 1/2 + 1/4 + 1/8..........1/n
# user = int(input("Enter a number: "))
# j = 1
# i = 1
# while i <= user:
#     # print(j/i)
#     total = j/i
#     print(total)
#     i*=2
# # print(total)s
#! parfect number------6 = 1+2+3 = 6
# user = int(input("Enter a number: "))
# add = 0
# for i in range(1,user):
#     if user % i == 0:
#         add += i
# if add == user:
#     print("parfect number")
# else:
#     print("Not parfect number")
#! check prime number--bangla::oi sonkha and 1 die vag gale oita prime number onno kono sonkha die vag jabena
# user = int(input("Enter a number: "))
# total = 0
# for i in range(1,user+1):
#     if user % i == 0:
#         total += 1
# if total == 2:
#     print("Prime number")
# else:
#     print("Not prime number")
#? serice print prime number 
#! important program
# user = int(input("Eneter a number: "))
# for i in range(1,user+1):
#     total = 0
#     for j in range(1,i+1):
#         if i%j == 0:
#             total += 1
#     if total == 2:
#         print(j)