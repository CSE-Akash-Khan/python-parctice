number = [1,2,3,7,9,12]
word = ["mango","apple","orange"]
mixed = ["mango",4,"apple",5,None]
fruits = ["mango","apple","orange","banaan"]
# print(mixed)
#!list access
# print(number[2])
#!list slicing as good as string slicing
# print(number[1:])
# print(number[1:5])
# print(number[1:6:2])   #todo: {start:stop:step}
# print(number[::-1])
# print(number[1::2])
#! exchange item
# mixed[1] = "banana"
# print(mixed)
# mixed[1:] = ["jackfruite","graps",7]
# print(mixed)
#? .........Methode.......
#! append methode
# fruits.append("graps")
# print(fruits)

# null_list = []
# null_list.append("mango")
# null_list.append("orange")
# null_list.append("graps")
# print(null_list)
#! insert methode
# mixed.insert(1,"orange")
# mixed.insert(3,"orange")
# print(mixed)
#! join two list
# fruits1 = ["mago","orange"]
# fruits2 = ["banana","graps"]
# fruits = fruits1 + fruits2
# print(fruits)
# print(fruits1 + fruits2)
#! extend methode
#todo: its add one list another list item
# fruits1 = ["mago","orange"]
# fruits2 = ["banana","graps"]
# fruits1.extend(fruits2)
# print(fruits1)
# #! add list inside list
# #Todo: different between append and extend
# fruits1.append(fruits2)
# print(fruits1)
#! delete data form list
# animal = ['tiger','lion','cow','fox','dog']
#! pop methode-----its delete by defoult last item from the list
# animal.pop()
# animal.pop(2)
# print(animal)
#! delete methode ----its work same as pop methode
# del animal[1]
# print(animal)
#! remove methode------>its important for the list
# animal.remove("fox")
# # animal.remove("ox")
# print(animal)
#!..............................................
#? append , extend , insetr -------this methode for add item into list
#? pop , del , remove --------------This metode for del item from the list
#! in keywords
# animal = ['tiger','lion','cow','fox','dog']
# if "cow" in animal:
#     print("cow is present")
# else:
#     print("its not in the list")
#!.........................................
#? more methode into list
animal = ['tiger','lion','cow','fox','dog','lion','dog','dog']
#! count methode
# temp = animal.count("dog")
# print(temp)
#! sort methode --------->its arrenge by order lists item
# number = [3,5,1,2,4,6,8,7]
# number.sort()
# print(number)
# animal.sort()
# print(animal)
#! sorted function-------->its not change our main list.this func make new sorted list
# number = [3,5,1,2,4,6,8,7]
# print(number)
# print(sorted(number))
#! clear methode------>its will be clear all item from the list
# animal = ['tiger','lion','cow','fox','dog','lion','dog','dog']
# animal.clear()
# print(animal)
#! copy methode-------->its make one more copy list
# animal = ['tiger','lion','cow','fox','dog','lion','dog','dog']
# animal_copy = animal.copy()
# print(animal_copy)
# print(animal)
#! join splite
#! split methode with list---->convert string to list
# user_info = "Akash khan".split()
# user_info = "Akash,khan".split(",")
# name,age = "Akash_khan 24".split() #list unpacking
# name,age = input("Enter your name and age: ").split()
# print(name,age)
# print(user_info)
# print(string)
#!join methode------->convert list to string
# country = ['i', 'love', 'my', 'country']
# add = (','.join(country))
# print(add)
# # print(add.replace(","," "))

# l = ["Orange","banana","jack froot","apple","graps","cucumber"]
# # l.extend((["lion","cow","fox"]))
# # print(l)
# d = l + ["lion","fox"]
# print(d)
#? for loop with list
# animal = ['tiger','lion','cow','fox','dog','lion','dog','dog']
# # for i in animal:
#     # print(i)
# #! while loop with list------->its value less
# i = 0
# while i<len(animal):
#     print(animal[i])
#     i += 1
#? list inside list or 2d list
# numbers = [[1,2,3],[4,5,6],[7,8,9,10]]
# print(numbers[2]) #position finding
# for i in numbers:
#     for sublist in i:
#         print(sublist)
#.............sublist position finding
# print(numbers[2][3]) #[postiton][inside position]
# string = ["Akash","Rans","Sohel","Naim"]
# print(string[2][0])
#! generate list with with renge function
# l = list(range(1,11))
# print(l)
# ! something more about pop methode
# item = list(range(1,21))
# return_item = item.pop() #pop methode je value remove kore seta abar return kore
# print(item)
# print(return_item)
#! index methode with list
number = [1, 2, 3, 4, 5, 6, 7, 8, 9,1]
# print(number.index(1,2)) #todo we are finding 2nd ones position
numbers = [1, 2, 3, 4, 5, 1, 6, 7, 8, 9,1]
print(numbers.index(1,2,8)) #todo: position,start,stop
#? pass list to a function
# def negative_value(l):
#     revarse_store = []
#     for i in l:
#         revarse_store.append(-i)
#         # print(revarse_store)
#     return revarse_store
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# assign = negative_value(number)
# print(assign)
