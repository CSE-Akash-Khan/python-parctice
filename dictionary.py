
#! dictionary is a data structure
#? wahy we use dictionary
#todo: answer: because limition of lists, list are not enough to represent real data
#? what are dictionary
#todo: unorder collention of data key : value pair
#!how to create dictionary
# user = {'name' : 'Akash', 'age' : 20}
# print(user)
# print(type(user))
#! second methode to create dictionary
# user1 = dict(name = 'akash khan',age = 20)
# print(user1)
#! how to access data from dictionary
# user = {'name' : 'Akash', 'age' : 20}
# print(user['age'])
#? which type of data a dictionary can store
# its can store anything string,list,dictionary
#!................
# user_info = {
#     'name' : 'Akash',
#     'age' : 20,
#     'fav movie':['3 idiot','bang bang','kabikhusu kabi gum'],
#     'fav tunes' : ['inna sona kew','hum tumhare sanam']
# }
# # print(user_info)
# print(user_info['fav movie'])
#! dictionary under dictionary
# user_info2 = dict(
#     dict(
#         name = 'sohel',
#         age = 24,
#         fav_movie = 'fifty shede darker'
#     )
# )
# print(user_info2)
#! how to add data to empty dictionary
# empty_dict = {}
# empty_dict['name'] = 'akash'
# print(empty_dict)
#! key and value chaeck
user_info = {
    'name' : 'Akash',
    'age' : 20,
    'fav movie':['3 idiot','bang bang'],
    'fav tunes' : ['inna sona kew','hum tumhare sanam']
}
#todo: key check
# if 'name' in user_info:
#     print("present")
# else:
#     print("not present")
#todo: value check
# if 20 in user_info.values():
# if ['inna sona kew','hum tumhare sanam'] in user_info.values():
#     print("present")
# else:
#     print("not present")
#! loop in dictionary
# for i in user_info.values(): #todo: only value print
# for i in user_info: #todo: only key print
    # print(i) 
    # print(f"{i} : {user_info[i]}") #todo: key value both print
    # print(user_info[i]) #todo: another way print vlaue
#!key and value methode
# user_info_value = user_info.values()
# print(user_info)
# print(type(user_info_value))
# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))
#! item methode----its return all key value as a tuple
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))
#todo: for loop with item methode
# for key,value in user_info.items(): #todo: here is working tuple unpacking
#     print(f"your key is : {key} and value is : {value}")
#!pop methode->it's delete only value & return poped items and its type dependent on his value
# user_info = {
#     'name' : 'Akash',
#     'age' : 20,
#     'fav movie':['3 idiot','bang bang'],
#     'fav singer' : ['arjit sing','atif aslam'],
# }

# pop_item = user_info.pop('fav tunes')
# print(type(pop_item))
# print(user_info)
# print(f"pooped item is {pop_item}")
#!pop item methode----->its randomly delete key and value and return that item by tuple type
# pop_item_mehode = user_info.popitem()
# print(user_info)
# print(f"removed item {pop_item_mehode}")
# print(f"remove items type {type(pop_item_mehode)}")
#!update dictionary---->means you can add key value or rename value
# user_info = {
#     'name' : 'anik khan',
#     'age' : 20,
#     'country' : 'Bangladesh',
#     'sex' : 'Male'
# }
# more_info = {'hight' : '5f 7 inch','weight' : '50 kg','weight' : '70 kg'}
# # user_info.update(more_info)
# user_info.update({'name' : 'sohel rana','age': 24})
# print(user_info)
#! fromkey methode---its make all keys same value
# d = dict.fromkeys(['name','age','sex'],'unknown')
# d1 = dict.fromkeys('abc','unknown')
# d2 = dict.fromkeys(range(1,11),'unknown')
# d3 = dict.fromkeys(('name','age','sex'),('unknown','unknown2'))
# print(d3)
#! get methode
# user_info = dict(
    # name = 'Akash khan',
    # age = 21,
    # sex = 'Male',
    # fav_singer = ['arjit sing','atif aslam']
# )
# print(user_info['name']) #todo: if key is't in dict it's return error
# print(user_info.get('fav_singer')) #todo: if key is't in dict it's return none
# print(user_info.get('names','not found !')) #TODO: amra none er priborte onno kise oo return korate pari
#! clear methode ------->its clean all key and value
# user_info.clear()
# print(user_info)
#! copy methode
# d = user_info.copy() #todo: d and user info not same dictionary
# d1 = user_info #todo: d1 and user info same dictionary
# item = d1.popitem()
# print(f"poped item {item}")
# # print(f"its value of d :{d}")
# print(f"its value of d1 :{d1}")
# print(f"its value of user info: {user_info}")
#todo: its can be check
# if d1 is user_info: #TODO: tis check bouth dict is same memory place or not
#     print("true")
# else:
#     print("false")
# print(d == user_info) #TODO: its check value
#! character count
# def char_count(d):
#     char_store = {}
#     for char in d:
#         char_store[char] = d.count(char)
#     return char_store
# print(char_count('akash khan'))
#!...............................................
##function with dict
# def dict(d):
#     for i,j in d.items():
#         print(f"{i} : {j}")
# d = {'name' : 'akash','age' : 20}
# call = dict(d)