
# #! basic discassion
# def square(a):
#     return a**2
# # d = square(5) #basic way
# # print(d)
# s = square #we can call also this way
# print(s(5))
# print(s.__name__) #same output
# print(square.__name__) #same output
# print(s) #same memory location
# print(square) #same memory location
#! function as argument---using map function
'''bangla:- map function muloto kaj kore je vabe ta niche dekhano hoyese'''
#todo: normal way
'''ekhane l theke ekta kore item uthano hoyese r square function a pass korano hoyse(r ei kajti korese for loop)
  r square funtion prutibare ja return korese ta ekta khali list e add kora hoyese pore oi list take print kora hoyse
  map function muloto backend e evabe kaj kore niche personal map function toiri kore ta dekhano hoyese'''
# l = [2,3,4,5,6,7]
# def square(a):
#     return a**2
# print(list(map(square,l)))
#todo: use lamda function
# print(list(map(lambda a : a**2,l)))
#todo: we will make own map function
# def my_map(func,l):
#     '''func parametar take a function as argument'''
#     empty = []
#     for i in l:
#         empty.append(func(i))
#     return empty
# print(my_map(lambda a : a**2,l)) #todo: heres my_map and map working same
#todo: using list comp
# def my_map2(square,l):
#     return [square(i) for i in l]
# print(my_map2(lambda a : a**2,l))

#! functon return function----this type function called closer function or first class function
# def outer_func():
#     def inner_func():
#         print("hello world")
#     return inner_func
# var = outer_func() #todo: called outer func and return inner func. but inner func not called.now inner func store in var(variable)
# var() #todo: heres called inner function

#! practice closer functon or first class function
# #todo: by this func we can calculate numbers any power
# def power(x): #3
#     def number(n): #2
#         return n**x #todo: 2**3
#         # print(n**x)#?
#     return number
# # var = power(3) #store number #?
# # var(2) #called number #?
# cube = power(3) #todo: pass argument into power and power returned number
# print(cube(2)) #todo: pass argument into number and print number**power
# #..............................
# square = power(2)
# print(square(3))
# #.....................
# _4th = power(4)
# print(_4th(2))

#? ---------------------decorator------------------------------------------------------
#?------enhance the functionality of other function-------------------------------------
# def decorator_function(function):
#     def wrapper_func():
#         print("This is awesome function")
#         function()
#     return wrapper_func
# #i want to print with this function one more sentence:example- this is awesome function
# def func1(): # i want to enhance the function but without change
#     print("This is func 1")
# #i want to print with this function one more sentence:example- this is awesome function
# def func2():
#     print("This is func 2")

# #todo: declaration way
# # var = decorator_function(func1) #stored in var wrapper funciton
# # var() #wrapper function called
# #.....................................................................
# # func2 = decorator_function(func2) #its also right
# # func2() #called wrapper function
# #..........................................
# @decorator_function #its shortcut
# def func3():
#     print("This is funciton 3")
# func3()
#! solve some problem form decorator
# def decorator_function(func):
#     print("This is awesome function")
#     def wrapper_func(*args,**kwargs):
#         '''this is wrapper func'''
#         return func(*args,**kwargs) #always you have to return this is batter way
#     return wrapper_func
# @decorator_function
# # def func1(a):
# #     print(f"This is {a}")
# # func1(5)
# #......................
# def func2(a,b):
#     '''this is func 2'''
#     return a+b
# print(func2(8,4))#todo: actully heres calling not func2.heres calling wrapper func
# #todo:-----prove
# print(func2.__doc__) #output::-this is wrapper func
# print(func2.__name__) #output::-wrapper func

#! how to print func2 doc string
# from functools import wraps
# def decorator_function(func):
#     @wraps(func)
#     def wrapper_func(*args,**kwars):
#         '''This is wrapper funciton'''
#         return func(*args,**kwars)
#     return wrapper_func
# @decorator_function
# def add(a,b):
#     '''This function add two numbers'''
#     return a+b
# print(add.__doc__)
# print(add.__name__)
# print(add(5,4))
#! decorator practice
# from functools import wraps
# def print_function_data(any_function):
#     @wraps(any_function)
#     def wrapper(*args,**kwargs):
#         print(f"you are calling {any_function.__name__} function")
#         print(any_function.__doc__)
#         store = any_function(*args,**kwargs) #todo heres called function and stored theie return value
#         return store #todo so heres dont needed to call funciton again becouse function called before
#     return wrapper

# @print_function_data
# def add(a,b):
#     '''The function takes two number as parameters and return their sum'''
#     return a+b
# print(add(4,5))
#! exercise 1
# from functools import wraps
# import time
# def calculate_time(any_function):
#     @wraps(any_function)
#     def wrapper(*args,**kwargs):
#         print(f"executing....{any_function.__name__} function")
#         t1 = time.time()
#         returned_value = any_function(*args,**kwargs)
#         t2 = time.time()
#         total_time = (t2 - t1)
#         print(f"This function took {total_time} seconds to run")
#         return returned_value
#     return wrapper

# @calculate_time
# def square(n):
#     return [i**2 for i in range(1,n+1)]
# square(10)
# # print(square(10))
#! python practice 2
# #todo: this decorator funciton take argument as a int. if another data type pass the decorator then return invalid argument
# from functools import wraps
# def only_int_allow(function):
#   @wraps(function)
#   def wrapper(*args,**kwargs):
#     if all([type(i) == int for i in args]): #todo: use list comp and its easy
#       return function(*args,**kwargs)
#     # data_type = [] #todo: normal way
#     # for i in args:
#     #   data_type.append(type(i)==int) #todo: heres return true or false
#     # if all(data_type): #todo: that means all.. 1--or--True---bangla:jodi sob True hoy then return function
#     #   return function(*args,**kwargs)
#     else:
#       return "invalid argument"
#   return wrapper
# @only_int_allow
# def add_all(*args): ``
#   total = 0
#   for i in args:
#     total += i
#   return total
# print(add_all(1,2,3,4,4))
#! one step deep in decorator funciton
# def only_data_type_allow(data_type):
#     from functools import wraps
#     def decrator(any_function):
#         @wraps(any_function)
#         def wrapper(*args,**kwargs):
#             if all([type(i) == data_type for i in args]): #todo: if i == datatype then return true else return false
#                 return any_function(*args,**kwargs)
#             else:
#                 return "invalid argument"
#         return wrapper
#     return decrator

# @only_data_type_allow(str)
# def string(*args):
#     store = ""
#     for i in args:
#         store += i
#     return store
# print(string("akash","khan"))