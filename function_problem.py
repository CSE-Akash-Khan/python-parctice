# def grater(num1,num2):
#     if num1 > num2:
#         return num1 
#     return num2
# a,b = int(input("Enter first number: "))
# # b = int(input("Enter second number: "))
# bigger = grater(a,b)
# print(f"{bigger} is grater")
#! problem 2
# def revarse(num):
#     return num == num[::-1] 
# user = input("Enter a sentence: ")
# temp = user.upper()
# # user.upper()
# print(revarse(temp))

#? solve problem from book
# #!problem 1
# def grater(a,b,c):
#     if a>b:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c
# a,b,c = map(int, input("enter three number: ").split(","))
# # d = int(a)
# # e = int(b)
# # f = int(c)
# print(grater(a,b,c))
# #!problem 2.. gcd of two number---gcd: greatest common number
# def gcd(a,b):
#     if b>a:
#         gcd(b,a)
#     while b != 0:
#         reminder = a%b
#         a = b
#         b = reminder
#     return a
# # user1,user2 = map(int,input("Enter two number space separated: ").split(" "))
# # print(gcd(user1,user2))
# #!problem 3.... lcm--->least common multiple
# def lcd(x,y):
#     # return lambda gcd(x,y) : (x+y)/gcd
#     store = gcd(x,y)
#     return (x*y)//store
# # print(lcd(12,18))
# user1,user2 = map(int,input("Enter two number space separated: ").split(" "))
# print(lcd(user1,user2))
#! problem 4..prime number
# def prime_number(a):
#     total = 0
#     for i in range(1,a+1):
#         if a % i == 0:
#             total+=1
#     if total == 2:
#         return "This is prime number"
#     return "this is composite number"
# user = int(input("Enter a number: "))
# print(prime_number(user))
#!.......jsut paractice
# def prime_seq(x):
#     for i in range(1,x+1):
#         counter = 0
#         for j in range(1,i+1):
#             if i % j == 0:
#                 counter += 1
#         if counter == 2:
#             print(j)
# print(prime_seq(20))
