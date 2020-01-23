
#?......lamda expression(anonymous function)...............
#? ......you have to intension on INPUT AND RETURN..........
#todo: this function has no name its use with built in func, map,reduce,filter, etc
#!...........................
#todo: simple way
# def add(a,b):
#     return a + b
# #todo: use lamda
# add2 = lambda a,b : a+b
# print(add2(5,4))
# multi = lambda a,b : a*b
# print(multi(3,4))
##........print one line
# print((lambda a,b : a**b) (5,2)) #todo: value define in one line
#! actually its use when we need to send a function as a argument for another function
# def my_func(func,a,b):
#     return func(a,b)
# print(my_func(lambda a,b : a+b,10,20))
# #todo: prove anonymous(it has no name)
# print(add) #it has name 
# print(add2) #but it has no name so it is anonymous
# print(multi)
# #?output
# # <function add at 0x009E0810> #todo: here name of func
# # <function <lambda> at 0x00A494B0> #todo: but heres no name of func
# # <function <lambda> at 0x00A494F8>
#! lamda practice
# # easy way
# def is_even(a):
#     return a % 2 == 0
# print(is_even(8))
#....................................
# # use lamda
# is_even2 = lambda a : a%2 == 0
# print(is_even2(5))
#todo: input last char
# # easy way
# def las_char(char):
#     return char[-1]
# print(las_char("akash"))
#...............................................
# #use lamda
# las_char2 = lambda word : word[-1]
# print(las_char2("akash"))
#! lamda with if else
# #easy way
# def func(char):
#     if len(char) > 5:
#         return True
#     return False
# print(func("rana"))
#.................................................................0
# #use lamda
# func2 = lambda word : True if len(word)>5 else False
# print(func2("akash khan"))
# #use without if else
# func3 = lambda name : len(name) > 5
# print(func3("sohel rana"))

#?.................enumerete function...................
#?............we can get items position by this...........
# todo: easy way
# l = ["akash","rasel","sazzad"]
# # pos = 0
# for i in l:
#     # print(f"{i} : {pos}") #todo: or
#     print(f"{i} : {l.index(i)}")
#     # pos += 1
#todo: use enumerete function
# l = ["akash","rasel","sazzad"]
# for pos,i in enumerate(l):
#     print(f"{i} : {pos}")
#todo: exerxcise----if pass string--output--str(position)--else--(-1): use unumerete
## easy way
# def func(string,l):
#     if string:
#         return f"{string} : {l.index(string)}"
#     return -1
# l = ["akash","rasel","sazzad"]
# print(func("sazzad",l))
#...........................................
## use enumerete func
# def func(string,l):
#     for pos,i in enumerate(l):
#         if i == string:
#             return pos
#     return -1
# l = ["akash","rasel","sazzad"]
# print(func("rasel",l))

#?...............map function...its iterator...................
#?.......take function and argument as a iterator........
# number = [1,2,3,4,5]
# def square(a):
#     return a**2
# # print(square(1))
# # print(square(2)).(3),(4)....
# #todo: same problem we can do by map function
# number = [1,2,3,4,5]
# def square(a):
#     return a**2
# print(map(square,number)) #its return object
# print(list(map(square,number))) #you have to convert list or tuple
#todo: another smart way use map function---we can list comp for this
# number = [1,2,3,4,5]
# square3 = list(map(lambda a : a**2,number))
# print(square3)
#todo: actually we use it with pre define function example:
char = ['abc','abcd','abcde','abcdef'] #we need this len
##simple way
# len_char = [len(i) for i in char]
# print(len_char)
##use unemerete function
##use map
# len_char = list(map(len,char))
# print(len_char)
#todo: we can use loop with map func..but one time
# char = ['abc','abcd','abcde','abcdef'] #we need this len
# func = map(len,char)
# for i in func:
#     print(i)
# for j in func:
#     print(j)
#? .............filter function....its iterator............
#?/...if only return condition true...then its return variables item other wise its not return
# number = [1,2,3,4,5,6,7,8,9,10]
#todo: use filter function
# even_num2 = tuple(filter(lambda a : a%2 == 0,number))
# print(even_num2)
##use map
# even_num = tuple(map(lambda a : a%2 == 0,number)) #todo: its returned boolean
# print(even_num)
#.......................................
# print(list(filter(lambda a : a%2==0,list(range(1,11))))) #bangla: je item er karone function false return korbe se item ta bad
# #todo: we can do same program use list comp
# even_num3 = [i for i in number if i%2 == 0]
# print(check)
# print(even_num3)
#todo: for loop with filter
# number = [1,2,3,4,5,6,7,8,9,10]
# func = filter(lambda a : a**2,number)
# for i in func:
#     print(i)

#? ....................zip functon.....ites iterator..................
#?..its make pair different variables item..and return as a tuple..........
#todo: create zip
# user_id = ['user1','user2','user3']
# # user_id = ['user1','user2'] #todo: its work with small variable
# user_names = ['akash','sohel','rana']
# user_title = ['khan','halwlader','boxsho']
# print(list(zip(user_id,user_names)))
# print(list(zip(user_id,user_names,user_title)))
#todo: convert tuple to dictionary
# example = [('a',1), ('b',2) ,('c',3)]
# print(dict(example))
#.................................................
# print(dict(zip(user_id,user_names)))
# print(dict(zip(user_id,user_names,user_title))) #todo: its not possible becouse here once tuple 3 tiems, only we can change tuple to dict once tuple 2 items
#todo: convert dictionary to tuple----its return dictionaries key
# example2 = {'a': 1, 'b': 2, 'c': 3}
# print(tuple(example2))
#! zip function part 2
# l1 = [1,3,5,9]
# l2 = [2,4,6,8]
#todo:................................
# l = [(1, 2), (3, 4), (5, 6), (7, 8)] #todo: we have to reverse
# # print(list(zip(*l)))
# l1,l2 = list(zip(*l))
# print(list(l1))
# print(list(l2))
#todo: grater use zip function
# grater = []
# for pair in zip(l1,l2):
#     grater.append(max(pair))
# print(grater)

#! avarage use as normal way by zip function-->from every list pick up on element and return their avarage
# def avarage(*args):
#     empty = []
#     for pair in zip(*args):
#         empty.append(sum(pair)/len(pair))
#     return empty
# d = [1,3,5,6,7],[3,5,6,7,8],[3,5,6,7,8]
# print(avarage(*d))
# #todo: use list comp use by zip function
# comp = lambda *args : [sum(i)/len(i) for i in zip(*args)]
# print(comp([1,3,5,6,7],[3,5,6,7,8]))

#?----------------any and all function-------------------------------
#todo: all function----->its work like as and gate ----if all 1 that meand True..then return True..else return 0--False
#? all funciton == all 1--or--true
# nummber1 = [2,4,6,8,10]
# # nummber1 = [2,4,6,8,9]
# comp = all([i%2 == 0 for i in nummber1])
# print(comp)
#.....................................................
#todo: any function its work like as or gate --if any data 1--True then return true
# nummber1 = [1,3,5,7,3]
# nummber1 = [1,3,5,9,7,2]
# comp = any([i%2 == 0 for i in nummber1])
# print(comp)
#! any all function practice
#todo: normal way
# def summation(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# print(summation(24,5,6,7,7.5,"akash")) #todo: heres some problem if you pass string then out put will be error
#todo: use all function----this way can fix output error
# def add(*args):
#     if(all([(type(i) == int or type(i) == float) for i in args])):
#         total = 0
#         for i in args:
#             total += i
#         return total
#     return "Wrong input"
# print(add(24,5,6,7,7.5,'akash',[1,2,3,4]))
# print(add(24,5,6,7,7.5))

#?----------------------min and max function-------------------------
#? ........................advance....................................
#! normal use min and max functon
# l = [2,7,9,5,3]
# print(max(l))
# print(min(l))
#! advance practice
# name = ["akash khan","rana","sohel rana"]
# print(min(name, key = lambda item : len(item))) #todo: ekhane key use kore dekhano hoyse (hindi):kiske according min or max print korete hobe
# ............................................
# information = [
#     {'name' : 'akash', 'score':90, 'age':20},
#     {'name' : 'rana', 'score':80, 'age':20},
#     {'name' : 'naim', 'score':70, 'age':20},
#     {'name' : 'sohel', 'score':60, 'age':24}
# ]
# print(max(information, key = lambda item : item.get('score'))['name'])#todo: heres return value
# print(max(information, key = lambda item : item.get('score')).get('name','not found!'))
# .................................................................
# student = {
#     'akash' : {'score' : 91,'age':20},
#     'naim' : {'score' : 92,'age':20},
#     'rana' : {'score' : 93,'age':20}
# }
# print(max(student, key = lambda item : student[item]['score'])) #todo: heres returned key

#?---------------------- Advance sorted function----------------------
#todo:actually its use with list
# l = ['banana','orange','apple']
# l.sort()
# print(l)
#todo: use with tuple
# t = ('banana','orange','apple')
# t.sort() #its not possible becouse tuple are immutable
# print(t)
##..... but we can use sorted funciton
# store = sorted(t) #todo: its not change main tuple its make new tuple
# print(store)
#.....................................
# s = {'banana','orange','apple'} #its work same like as tuple
# store = sorted(s)
# print(store)
# #! advance sorted function
# car = [
#     {'name' : 'bmw', 'price' : 250000},
#     {'name' : 'marcetege', 'price' : 230000},
#     {'name' : 'lambor green', 'price' : 270000},
#     {'name' : 'toyeta', 'price' : 220000},   
# ]
# print(sorted(car, key = lambda item : item['price'],reverse = True))

#?........................ dock string print.....................
#? actually what is dock string..its print functions discription
def func(a,b):
    '''its take two input and return their sum'''
    return a+b
# print(func.__doc__)
# print("......................")
# print(len.__doc__)
# print("......................")
# print(sum.__doc__)
# #! bangla:: upare je je function poresi sob gular doc print kora holo
# print("........enumerate..............")
# print(enumerate.__doc__)
# print("........map..............")
# print(map.__doc__)
# print("........filter..............")
# print(filter.__doc__)
# print(".........zip.............")
# print(zip.__doc__)
# print(".........all.............")
# print(all.__doc__)
# print(".......any...............")
# print(any.__doc__)
# print(".........mini.............")
# print(min.__doc__)
# print("......................")
# print(max.__doc__)
# print("........sorted..............")
# print(sorted.__doc__)

#!help function
#! if we forgot whay use this function or actullay don't know which type of work complete this functon
#! then we can use for helping help functon
# print(help.__doc__)
# help(sum)

