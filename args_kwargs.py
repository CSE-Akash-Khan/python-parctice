
#! **args----its can be called flexible function
#? its can be take many more argument and return as a tuple
# def add_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# print(add_all(1,3,45,6,7))
#todo same work without args
# def add_all(num):
#     total = 0
#     for i in num:
#         total += i
#     return total
# number = 1,3,45,6,7 #todo: first time need to store number any variable then its passed
# print(add_all(numberd))
#! args with normal parametar
# def multiply(num*args):
#     print(num)
#     print(args)
#     print(type(args))
#     multi = 1
#     for i in args:
#         multi *= i
#     return multi
# print(multiply(3,2,6))
#! args as a argument
# def argument(*args):
#     total = 1
#     for i in args:
#         total *= i
#     return total
# multi = [1,2,3]
# print(argument(*multi)) #todo: list unpacking....here anything will be unpacked
# # print(argument(multi))

#!................................................
#? kwargs(key word and argument) its take key and word and return as a dictionary
# def key_word(**kwargs):
#     for i,j in kwargs.items():
#         print(f"{i} : {j}")
#         # print(dept)
# # dictionary = {'name':'akash khan','age' : 20}
# # key_word(**dictionary) #todo: dictionary unpacking
# key_word(**{'name':'akash khan','age' : 20})
# # key_word(name = "akash khan",age = 24)
# #todo: if you want to pass extra argument then you have to define extra parametar under the function
# # key_word('computer',name = "akash khan",age = 24)

#!..........function with all parameters.............
#todo: parameters diclaretion has some order
#? parameters
#? args
#? defult parameters
#? kwargs
#todo: memories formula:--- PADK: P=parameter,A=*args,D=defult argument,K=**kwargs
# def func(name,*args,last_name = "khan",**kwargs):
#     print(name)
#     print(*args)
#     print(last_name)
#     print(kwargs)
# func("Akash",1,2,3, a = 1,b = 2)
#?..........................................................
#? exercise 1
# def funck(num,*args):
#     if args:
#         return [i**num for i in args]
#     else:
#         print("hey you didn't pass")   
# args = [1,2,3]
# # print(funck(3,*args)) #todo: or
# print(funck(3,*[]))
#? Exercise 2
# def func(*args):
#     store = []
#     for i in args:
#         d = i.title()
#         store.append(d)
#     return store
# # name = ["akash","rana"]
# print(func(*["akash","rana","naim"]))
# # print(func(*name))
#todo: same problem use list comprehension
# def func(*args):
#     return [i.title() for i in args]
# # name = ["akash","rana"]
# print(func(*["akash","rana","naim"]))
# # print(func(*name))
#! same probelm with reverse_str input---rana---output-->Anar
# def func(names,**kwargs):
#     if kwargs.get("reverse_str") == True:
#         return [name[::-1].title() for name in names]
#     else:
#         return [name.title() for name in names]
# name = ["akash","rana"]
# print(func(name)) #todo: heres call else statement
# print(func(name,reverse_str = True)) #todo: and heres call if statement