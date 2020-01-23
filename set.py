''' set is a data type
    and its unorder collention of data
    you cant store here list or dictionary
    but we can strore int float none etc we can't index our data
    like list or dict'''

# s = {'akash',3,4.5,2,2,None}
# print(s)
# a = {1,3,5,6,7,3,5} #todo: its print only unic data
# print(type(a))
# print(a)
#? why we use set---->it's remove duplicate data
# l = [1,1,2,2,3,4,5,5,6,6,7,8,9,9]
# s = list(set(l))
# print(s)
#! add methode-----> its add data in set
# s = {1,2,3}
# s.add(4)
# s.add(5)
# s.add(5)
# print(s)
#! remove methode----->its remove data from set
# s = {1, 2, 3, 4, 5}
# s.remove(7) #todo: if you give data which not in list then give a error
# s.remove(5)
# print(s)
#! discard methode----->its not give any error 
#? its batter
# s = {1, 2, 3, 4, 5}
# s.discard(3)
# s.discard(9)
# print(s)
#! clear methode
# s = {1, 2, 3, 4, 5}
# s.clear()
# print(s)
#! copy methode
# s = {1, 2, 3, 4, 5}
# s.copy()
# print(s)
#! pop methode -----> its remove first item from the set and its return
# s = {'mango','apple','banana'}
# store = s.pop()
# print(store)
#! len function
# s = {'akash',3,4.5,2,2,None}
# print(len(s))
#! when we diclear null set
# temp = set() #todo its write way
# tem = {} #todo its wrong way becuse we diclear dict this way
#! more about set mehtode
# l = [1, 2, 3, 4, 5, 3, 4, 1]
# print(list(set(l)))
#todo: check item in set
# s = {1, 2, 3, 4, 5, 3, 4, 1}
# if 2 in s:
#     print("Present")
# else:
#     print("Not present")
#! set union----> its filter uniq item between tow set
# s1 = {1,2,3,4,5}
# s2 = {6,7,8,1,2,5}
# union = s1 | s2
# print(union)
#! intersection----->its filter common number
# intersection = s1 & s2
# print(intersection)
#! we can do this same work by using methode
#todo: uniton methode
# a = {1,2,3,4,5}
# b = {6,7,8,1,2,5}
# print(a.union(b))
#todo: intersention methode
a = {1,2,3,4,5}
b = {6,7,8,1,2,5}
# print(a.intersection(b))
#! difference methode---->example: a - b or b - a
print(a.difference(b))
print(b.difference(a))