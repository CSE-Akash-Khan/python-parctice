
#! explain generator 
#? its a iterator...its take one argument at a time--its reduce memory space and safe time--actually its also a sequence like as list
#? but list first time relode all data then take many operation so here lost many memory space and time..but generator relode one data and take their action
#? according to command after complete action they take next data and deleted previous data from memory..this way work generator
#! example
#? list = [1,2,3,4,5]
#? generator = (1) after delete 1 (2) after delete (3)..........
#!.................................................................................................................
#! How to define generator
# def num(n): #todo:now its not a function its a generator
#     for i in range(1,n+1):
#         yield i #todo: yield is a key word. its work insted of return but not return key word.its return one by one data at a time
#...................................................................
# values = num(10)
# # print(values) #todo: its returned object output::<generator object num at 0x00648D70>
#.......................................................................
# print(values.__next__()) #output:--1
# print(values.__next__()) #output:--2
# #? for call next function again and again..we use for loop..its handale all iterator and iterable..
# #? when take for loop iterable..first time he call "iter function" and make iterables as a iterator
# #? then call "next funciton" according to range....and when for loop take iterator directly he call next function.
# #?don't needed to call iter function. becouse he is already iterator.
# for i in values:
#     print(i)

#!take another example
# def square(n): #todo: generator
#     for i in range(1,n+1):
#         yield i
# for i in square(10):
#     print(i**2)
#! if 2 or many time we call generator...then what will be happend...lets see
# def square(n): #todo: generator
#     for i in range(1,n+1):
#         yield i
# values = square(10)
# for i in values:  #todo: first time
#     print(i**2)
# for i in values: #todo: 2nd time
#     print(i**2)
# #? same out put becouse generator take data only one time..and after deleted data. so if i call many time same generator its will be print only one time
#! exercise
# def even_num(n):
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             yield i
#todo: ........shortcut way..................
# def even_generator(n):
#     for i in range(2,n+1,2):
#         yield i
#todo:......call generator...............
# even_num = even_num(10)
# for i in even_num:
#     print(i)
#----------------------------
# values = even_generator(10)
# for i in values:
#     print(i)
#?----------------------------------generator----------------------- comprehension------------------------------------------------
#! generator comprehension---->its too easy and like as list comprehension just parantheses insted of squar bracket
# squar = (i**2 for i in range(1,11)) #todo: maked generator
# # print(squar)
# for i in squar:
#     print(i)
# #...............................
# for i in squar:
#     print(i)
# # not changed

#?------------------------------------------- list vs generator-------------------------------------------
#! show the performance please see -----182 number tutorial

#todo: lets see how much time needed to run list and generator
# import time
#? ............for list.........
# t1 = time.time()
# l = [i**2 for i in range(1,10000000)] #10 million
# t2 = time.time()
# print(t2 - t1) #!same
#?..........for generator.............
# t1 = time.time()
# g = (i**2 for i in range(1,1000000)) #10 million
# print(time.time() - t1) #!same
