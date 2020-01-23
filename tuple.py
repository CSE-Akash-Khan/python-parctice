
#? tuple is a data structure and tuple are immutable we store fixed data type by tuple
#? tuple and string are immutable and we can use only type of methode which we can use with string
example = ('one','two','three')
# mixed = (1,2,3,'akash',None) #its tuple you can store any type data
# print(type(example))
#todo: no append,no insert,no pop, no remove
#todo: tuples are faster than list
#todo: its can be use: count metode, index methode, len function, slicing
# print(example[:2]) #slicing
# print(example.index("two")) #index methode
# print(len(example)) #len function
# print(example.count('two')) #count methode....example er vitor i koto bar ase
#! tuple with one element
# temp = ('Sohel') #its string
# print(type(temp))
# temp2 = ('Akash',) #its tuple
# print(type(temp2))
#! tuple with for loop ......>you can use while loop
# mixed = (1,2,3,'akash',None)
# for i in mixed:
#     print(i)
#! tuple without parametar
# fruits = 'mango','orange','banana','kiwi'
# print(type(fruits))
#!tuple unpacking
# fruits = ('mango','orange','banana') 
# fruits1,fruits2,fruits3 = fruits #how much element thouse much variable
# print(fruits1)
#!list inside tuple---------->we can pop append.ctc... with list inside tuple
# fruits = ('mango','orange','banana',['one','two','three']) 
# fruits[3].pop()
# fruits[3].append('Four')
# print(fruits)
#! some more methode we can use with tuples
number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(min(number))
# print(max(number))
# print(sum(number))
#! something more about tuple string and list
# mk_tuple = tuple(range(1,11))
# print(mk_tuple)
#todo: tuple can be make list
# _tuple = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(_tuple)
#todo: tuple can be make string
# _tuples = str((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(_tuples) #todo: output:"(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)" but its hidden""
# print(type(_tuples))
