# for i in range(10):
#     print(f"hello world {i}")
#! ............
# for i in range(1,11): 3 #todo: range means i ki value kahase kaha tak jayegi
#     print(f"hello world {i}")
#! sum 1 to 10 number
# total = 0
# for i in range(1,11):
#     total += i
# print(total)
#! useing user input
# user = int(input("Enter a number which you want to sum: "))
# total = 0
# for num in range(1 , user + 1):
#     total += num
# print(total)
#! calculate sum of digit:
# user = input("Enter a number: ")
# total = 0
# for i in range(len(user)):
#     total += int(user[i])
# print(total)
#! sum input number easy way
# num = input("Enter number: ")
# total = 0
# for i in num:
#     total += int(i)
# print(total)
#! ask user name and count each character
# user = input("Enter your name: ")
# user_store = ""
# for i in range(0,len(user)):
#     if user[i] not in user_store:
#         user_store += user[i]
#         print(f"{user[i]} : {user.count(user[i])}")
#!try some easy way
#todo its faculity only for python
# num = input("Enter your name: ")
# store = ""
# for i in num:
#     if i not in store:
#         store += i
#         print(f"{i} : {num.count(i)}")
#! exercise number guessing
# import random
# winning_number = random.randint(1,100)
# total = 1
# while True:
#     user = int(input("Guess a number between 1 to 100: "))
#     if winning_number == user:
#         print(f"you are win in {total} times")
#         break
#     else:
#         if winning_number < user:
#             print("you are too high")
#         else:
#             print("you are too low")
#     total += 1
#     continue
#! Another rules 
#todo: its batter rule
# import random
# guess_number = random.randint(1,50)
# total = 1
# number = int(input("Guess a number between 1 to 50: "))
# game_over = False
# while not game_over:
#     if guess_number == number:
#         print(f"you guess the number in {total} times")
#         game_over = True
#     else:
#         if guess_number < number:
#             print("you are too high")
#         else:
#             print("you are too low")
#         total += 1
#         number = int(input("guess again: "))
#! For loop with string in easy way
#! old system
# name = "Khan Akash"
# for i in range(len(name)):
#     print(name[i])
#Todo: New system 
#? This faculity only for python because python string itreable
# name = "Akash"
# for i in name:
#     print(i)

# for i in "sohel":
#     print(i)
#! step argument in for loop
# for i in range(1,11,2):
#     print(i)
#!.......
# for i in range(10,0,-1):
#     print(i)
# for i in range(-1,-10,-1):
#     print(i)
# for i in range(1,11):
#     pass
# else: #todo: amra je kono loop ee loop er por else statement lagate pari
#     print("The loop is over")

#! preactice inner loop
# total = 0
# for i in range(1,3): #todo: first loop ekbar cholle 2nd loop 3 bar cholbe
#     for j in range(1,4):
#         total += i + j
#         print(i,j,total)
# # print(total)
#! break keyword and continue
# for i in range(1,11):
#     if i == 6:
#         break
#     print(i)
# print(".....continue keyword......")
# for j in range(1,10):
#     if j == 5:
#         continue
#     print(j)
#! in keyword
# name = input("Enter your name: ")
# Name = name.upper()
# if "A" in Name:
#     print("A is present")
# else:
#     print("A is not present")
