
#? Actually list comp you have to think about append
#! square of number
# temp = []
# for i in range(1,11):
#     temp.append(i**2)
# print(temp)
# #todo: same work we will do by list comprehension
# list_1 = [i**2 for i in range(1,11)]
# print(list_1)
#! store every sentence first word
#todo: easy way
# l = ['akash','rana','naim']
# empty_list = []
# for i in l:
#     empty_list.append(i[0])
# print(empty_list)
#todo: its use list comprehension
# list_2 = [i[0] for i in l]
# print(list_2)
#! -1,-2, -3-----10 use list comprehension
# list_3 = [-i for i in range(1,11)]
# print(list_3)
#! list comprehension with if
#todo: easy way---->even and odd number
# l = list(range(1,11))
# empty_list = []
# for i in l:
#     if i%2 == 0:
#         empty_list.append(i)
# print(empty_list)
#todo: list comprehension
# list_2 = [i for i in range(1,11) if i%2 == 0]
# print(list_2)
# list_3 = [i for i in range(1,11) if i%2 != 0]
# print(list_3)
#! list compreshension with if else output--->-1,2*2,-3,4*2---10
#todo: easy way
# l = []
# for i in range(1,11):
#     if i%2 == 0:
#         l.append(i*2)
#     else:
#         l.append(-i)
# print(l)
#todo: use list comprehension
# list_comp = [i*2 if i%2 == 0 else -i for i in range(1,11)]
# print(list_comp)
#! nested list comprehension
#todo: easy way
# new_list = []
# for i in range(3):
#     new_list.append([1,2,3])
# print(new_list)
#todo............
# inside_list = [[1,2,3] for i in range(3)]
# print(inside_list)
# #todo: another way
# inside_list2 = [[i for i in range(1,4)] for i in range(3)]
# print(inside_list2)
# #todo.................
# inside_list3 = [list(range(1,4)) for i in range(3)]
# print(inside_list3)
#? exercise---1--->'akash','rana'  output--->'hsaka','anar'
# def reverse(l):
#     return [i[::-1] for i in l]
# user = input("Enter some name of your friends comma separated: ").split(",")
# users = list(user)
# # l = ['akash','rana','sohel']
# print(reverse(user))
#? exercise---2 input-->1,2,3,'akash' output-->'1','2','3','akash'
# def string(x):
#     empty_list = []
#     d = "aksah"
#     for i in x:
#         if type(i) != type(d):
#             empty_list.append(str(i))
#         else:
#             empty_list.append(i)
#     return empty_list
# l = ['akash',1,2,3,None,{'name':'akash'}]
# print(string(l))
# #todo: use list compreshension
# def string(l):
# #     return [str(i) for i in l if i != str]
#     return [str(i) for i in l if type(i) == int or type(i) == float]
# l = ['akash','rana',1,2,3,3.2,None,]
# print(string(l))

