
#! exercise 1
# def square_list(number):
#     total = []
#     for i in number:
#         total.append(i**2)
#     return total
# numbers = list(range(1,11))
# print(square_list(numbers))
#! exercise 2
# def revese(number):
#     temp = []
#     for i in range(len(number)):
#         store = number.pop()
#         temp.append(store)
#     return(temp)
# numbers = list(range(1,11))
# print(revese(numbers))
# #! another way
# def revarse(l):
#     return l[::-1]
# number = list(range(1,14))
# print(revarse(number))
#! another way
# def revese(l):
#     l.reverse()
#     return l
# number = list(range(1,11))
# print(revese(number))
#! Exercise 3
# def word(l):
#     null_list = []
#     for i in l:
#         null_list.append(i[::-1])
#     return null_list
# l = ['akash','abc','rana','naim']
# print(word(l))
#! Exercise 4
# def filter(number):
#     odd = []
#     even = []
#     for i in number:
#         if i % 2 != 0:
#             odd.append(i)
#         else:
#             even.append(i)
#     odd_even = [odd , even]
#     return odd_even
# numbers = list(range(1,11))
# print(filter(numbers))
#! Exercice 5
# def common_number(l):
#     null_list = []
#     common_num = []
#     for i in l:
#         for sub in i:
#             if sub not in null_list:
#                 null_list.append(sub)
#             else:
#                 common_num.append(sub)
#     common_num.sort()
#     return common_num
# two_list = [1,4,5,6] , [4,7,8,6,9,1]
# temp = (common_number(two_list))
# print(f"common number between two list is {temp}")
#! use two parametar into function
# def common_num(l1,l2):
#     output = []
#     for i in l1:
#         if i in l2:
#             output.append(i)
#     return output
# print(common_num([1,4,5,6] , [4,7,8,6,9,1]))
#! Exercise 6
# def inside_list(l):
#     total = 0
#     for i in l:
#         if type(i) == list:
#             total += 1
#     return total
# d = [1,2,3,[4,5],[7,8]]
# print(inside_list(d))
