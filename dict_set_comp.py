
#? actually dict comp you have to think about key and value
#!square of number use dict comp---- out put {1:1 2:4 3:9 4:16}
# square = {i : i**2 for i in range(1,11)}
# square = {f"square of {i} is" : i**2 for i in range(1,6)}
# for key,value in square.items():
#     print(key,value)
#! number counter use dict comprehension
#todo: easy way
# def counter(d):
#     empty_dict = {}
#     for i in d:
#         empty_dict[i] = d.count(i)
#     return empty_dict
# print(counter('akashkhan'))
#todo: use dict comprehension
# string = "akash khan"
# dict_counter = {num : string.count(num) for num in string}
# # print(dict_counter)
# for i,j in dict_counter.items():
#     print(f"{i} is {j} times")
#! dict comprehension with if else---->{1:odd , 2:even}
# odd_even = {i: ('even' if i%2 == 0 else 'odd') for i in range(1,11)}
# print(odd_even)

#?..............its like as set comp..............................
#? SET COMPREHENSION actually its use littel bit
#! square number use set comp
# set_comp = {i**2 for i in range(1,11)}
# print(set_comp)
#!gather every string first character
strings= "Akash","sohel","rana"
first_char = {string[0] for string in strings}
print(first_char)