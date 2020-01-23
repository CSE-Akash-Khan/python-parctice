
#! its give you multiply which number you will be enter
#! problem 1
# user = int(input("Enter a number: "))
# for i in range(1,11):
#     multi = user * i
#     print(f"{user} x {i} = {multi}")
#! same program using while loop
# user = int(input("Enter a number: "))
# count = 1
# while count <= 10:
#     print(f"{user} x {count} = {user*count}")
#     count += 1
#! problem 2
# my_list = []
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 != 0:
#         my_list.append(i)
# print(my_list)
#! problem 3
# number = 13,34,19,56,98,12,52,34,28,76,74,42,46,68,67,95,99
# my_list = []
# for i in number:
#     if i < 50:
#         my_list.append(i)
# print(my_list)
#! problem 4
# number = 13,34,19,56,98,12,52,34,74,42,46,68,67,95,99,99,13,19,34,67,56,42,46
# my_list = []
# for i in number:
#     if i not in my_list:
#         my_list.append(i)
#         # print(i)
# print(my_list)
#! problem 5
# user = int(input("How many square want to make: "))
# for i in range(user):
#     d = "*"
#     print(d*user)
#! problem 6
# user = input("Enter word: ")
# user = user.upper() 
# # user = user.casefold()  #todo: same kaj kore
# if user == user[::-1]:
#     print("yes it is palindrome")
# else:
#     print("Not palindrome")
#! problem 7
# user = int(input("Enter a number: "))
# my_list = [1,3,5,7,11,15,17,20,26,31,44,54,56,65,77,94,100]

# if user in my_list:
#     print(user)
# else:
#     print("its not in list")
#! ................
#! problem 8 onusiloni
# total = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         total += i
# print(total)
#! another rule
# total = 0
# i = 2
# while i <= 100:
#     total += i
#     i += 2
# print(total)
#! problem 9
# user = int(input("Enter a number: "))
# for i in range(user):
#     star = "*"
#     print(star*i)
#! problem 10
# my_list = []
# for i in range(1,101,2):
#     if i not in my_list:
#         my_list.append(i)
# print(my_list[0:30])
#! fibonacci serice
#todo: 0 1 1 2 3 5 8 13 21 ...........>
def fibonacci_seq(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b, end = " ")
    elif n == 0:
        print("you have to enter  upto 0 number")
    else:
        print(a,b, end = " ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b, end = " ")
user = int(input("Enter a number: "))
fibonacci_seq(user)