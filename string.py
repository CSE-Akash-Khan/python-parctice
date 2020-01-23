
#! escape sequence.py
# print("hello \"Akash\" khan")#back slash double code
# print('I\'m akash')
# print("this is double back slash\\\\") #how much back slash you want to print {n(squre)}theory
print("akash \n rana \n naim")#\n mean new line
# print("Akash\trana") # space
# print("hell\blo")

# #output:line a \n line b
# print("line a \\line b")
# #output: \" \'
# print("\\\" \\\'")
# #\' - ' (a)
# # \\ - \ (b)
# # ab - \\\' print(\')
# # ab - \\\" print(\")
#!string and input
# first_name = " Akash"
# last_name = "Khan"
# full_name = first_name + " "+ last_name
# # print(full_name + str(3))
# print(full_name + " anik")
# print(first_name*3)

# name = input("type your name: ")
# age = input("type your age: ")
# print("hello", name)
# print("your age is", age)

# number_1 = float(input("Enter first number: ")) #! or int input
# number_2 = float(input("Enter second number: "))
# total_number = number_1 + number_2
# print("your total is " + str(total_number))
#!string methode
# name = "Mohiuddin khan akash"
# case = "AkAsH kHaN"

# print(len(name)) #todo: len method
# print(case.upper()) #todo: upper method
# print(case.lower()) #todo: lower method
# print(case.title()) #todo: title method
# print(name.count("a")) #todo count method
#!..................................
# name = ("BanGla")
# print(name.swapcase())
# word = ("bangla")
# print(word.title()) #TODO  same 
# print(word.capitalize()) #TODO same

#! string mehtode exercise 3
# name,char = input("Enter the name and type one character using comma: ").split(",")
# length = len(name)
# first = char.upper()
# second = char.lower()
# total = first + second
# counting = name.lower().count(char.lower())
# counting = name.upper().count(char.upper())
# print(f"your name length is {length} and your typing charcter is {counting} times in this sentence")

# sentence = ("chak din chak chak din chak")
# print(sentence.count("c",1,5))
# print(len(sentence))
# # print(sentence.find("c",1))
#! string slicing
#todo: start and stop argument
# name = "Bangladesh"
# # print(name[:3]) #todo start : stop : step ....[ : : ]
# print(name[:5:-1])
# todo: step argument
# revarse = "amas"
# print(revarse[::-1])
# #todo: exersice 2
# name = input("What is your name: ")
# print(f"your name revarse is {name[::-1]}") #todo success full challange wow!
#! strip methode ------>its remove space
# name = "     Akash khan     "
# dots = ".........."
# print(name.lstrip() + dots) 
# print(name.rstrip() + dots)
# print(name.strip() + dots) #todo: strip methode its remove all the side space
# #! strip methode challange
# name,char = input("Enter your name and type one character from your name: ").split(",")
# length = len(name)
# counting = name.lower().count(char.lower().strip())
# print(f"your name length is {length} and typing character in your name {counting} times ")
 
# a,b,c = ("dhaka barisal sylhet").split()
# total = (a,b,c)
# print("-".join(total))
# #! String formating using c programming
# word = ("Bangla")
# print("My favorite language is: %s" %word)

# language_1 = ("Bangla")
# language_2 = ("English")
# print("My favorite language are: %s and %s" %(language_1,language_2))
#! replace and find & is finding
# string = "she is beautifull and she is good dancer"
# print(string.replace("is","was",1)) #todo is will be change with was and 1 means first is will change with was
# print(string.find("is",5)) #TODO "5" is which posotion will be start to find "is" position
# is_pos1 = string.find("is")
# is_pos2 = string.find("is",is_pos1 +1)
# print(is_pos2)
# print(string.replace(" ","_"))

# #! python 3 stirng formatting
# name = input("Enter your name :")
# age = int(input("Enter your age : "))
# print("hello {} your age is {}".format(name, age))

# #! python 3.6 string foematting
# print(f"hello your namr is {name} khan and your age is {age + 2}")
#! multiple variable
# name, age = "harshit",24
# print("your name is: " + name + " and your age is: "+str(age))
# a = b = c =1
# print(a+b) #todo multiple variable assing one value

# #! more input in one line
# name,age = input("Enter your name and age separated by comma: ").split(",")
# print("your name is: " + name + " and your age is: " + age)
#! exersice 1 chapter 1
# num_1,num_2,num_3 = input("Enter three number separated by comma: ").split(",")
# total_num = (int(num_1) + int(num_2) + int(num_3))/3
# print(f"total avarage is {total_num}")
# #? tinti int type variable keno comma separated newa jayna
# #! another try
# a = int(input("Entet first number: "))
# b = int(input("Enter 2nd number: "))
# total = a + b
# print(f"your total summation is {total}")
#! another way make string
# a = """bangla
# desh desh desh desh its replace again and again
# is a beautiful country"""
# print(a)