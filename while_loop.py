
#? while: that means == jokhon or jotokkhon
# i = 1
# while i <= 10:
#     print("Hello world")
#     i = i + 1
#! 1 to 10 every number sum using while loop
#! 0+1=1,1+2=3,3+3=6,6+4=10,10+5=15,15+6=21,21+7=28.........
# total = 0
# i = 1
# while i <= 10:
#     total = total + i #todo: total += i
#     i += 1 #todo: i = i + 1
# print(total)
#! exercise chapter 3, 1
# user = int(input("Enter the number which you want to sum: "))
# total = 0
# i = 1
# while i <= user:
#     total += i
#     i += 1
# print(total)
#! exercise 3 , 2
# user = input("Enter the number more then one digit: ")
# #256
# total = 0
# i = 0
# while i < len(user):
#     total += int(user[i])
#     i += 1
# print(total)
#! exercise 3 , 3
# user = input("Enter your name: ")
# temp_var = ""
# i = 0
# while i < len(user):
#     if user[i] not in temp_var:
#         temp_var += user[i]
#         print(f"{user[i]} : {user.count(user[i])}")
#     i += 1
#! AGAIN
# name = input("Enter your name: ")
# char_store = ""
# i = 0
# while i < len(name):
#     if name[i] not in char_store:
#         char_store += name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#     i += 1
#! solve problem from book
# i = 1
# total = 0
# while i <= 97:
#     total += i
#     i += 2
#     # print(total)
# print(total)

#! infenity loop
# while True:
#     print("Hello world")
#Todo: STOP THIS LOOP PRESS: CTRL + C
# i = 1
# while i > 0: #todo: its also infenity loop
#     i += 1
#     print(i)
