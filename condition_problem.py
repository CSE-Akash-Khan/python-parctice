# user = int(input("Enter value: "))
# if 10 > user:
#     if (user % 2) == 0:
#         print("less yes")
#     else:
#         print("less, no")
# else:
#     if 10 < user and (user % 3) == 0:
#         print("grater, yes")
#     else:
#         print("greater, no")

#! python 3 books problem
#! problem no 1:
# user = int(input("Enter the real number: "))
# if (user % 3) == 0 and (user % 5) == 0:
#     print("Yes")
# else:
#     print("No")
#! problem no 2:
# user = int(input("Please input the number: "))
# if user > 0:
#     print("Positive")
# elif 0 > user:
#     print("Negative")
# else:
#     print("Zero")
#! problem no 3:
# user = int(input("Please input the number: "))
# if (user % 2) == 0:
#     print("Even")
# else:
#     print("Odd")
#! problem no 4:
#? we number has sequence example 2 bigger then 1 but:character has sequence?
#TODO: ASCII code onusare print kora hoyese
# user = input("Type any character: ")
# if user >= "a" and user <= "z":
#     print("lower case")
# elif user >= "A" and user <= "z":
#     print("upper case")
# else:
#     print("Nothing")
#! problem no 5
# user1 = input("Enter any one character: ")
# user = user1.lower()
# if (user >= "a" and user <= "z"):
#     if user in "aeiou":
#         print("vowel")
#     else:
#         print("consonant")
# else:
#     print("Nothing")
#! problem no 6:
# user = int(input("Enter your launch bill: "))
# temp_1 = user//1000
# print(f"You have to pay 1000 takas note {temp_1} pice")
# temp_2 = user // 500
# print(f"You have to pay 500 takas note {temp_2} pice")
# temp_3 = user // 100
# print(f"You have to pay 100 takas note {temp_3} pice")
# temp_4 = user // 50
# print(f"You have to pay 50 takas note {temp_4} pice")
# temp_5 = user // 20
# print(f"You have to pay 20 takas note {temp_5} pice")
# temp_6 = user // 10
# print(f"You have to pay 10 takas note {temp_6} pice")
# temp_7 = user // 5
# print(f"You have to pay 5 takas note {temp_7} pice")
# temp_8 = user // 2
# print(f"You have to pay 2 takas note {temp_8} pice")
# temp_9 = user // 1
# print(f"You have to pay 1 takas note {temp_9} pice")
#! advance problem solve:
user = int(input("Please input your birth date: "))
if user % 4 == 0:
    print("Your birth date is leap year")
else:
    print("Your birth date is not leap year")
#! Advance problem solve 2:
# user = int(input("Enter your number: "))
# if user <= 100 and user >= 80:
#     print("Your grade is A+")
# elif user <= 80 and user >= 70:
#     print("Your grade is A")
# elif user <= 70 and user >= 60:
#     print("Your grade is A-")
# elif user <= 60 and user >= 50:
#     print("Your grade is B")
# elif user <= 50 and user >= 40:
#     print("Your grade is C")
# elif user <= 40 and user >= 33:
#     print("Your grade is D")
# else:
#     print("You are fail")