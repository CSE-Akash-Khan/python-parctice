# name = "Akash khan"
# print(len(name))
# print(name.center(14,"*"))

#! Make simple program
# name = input("Enter your name: ")
# print(name.center(len(name) + 4, "*"))

name = input("Enter your name: ")
symbol = input("Enter your symbol which you want to add in your name: ")
add = int(input("How many symbol you want to add in your name: "))
print(name.center(len(name) + add,symbol))

