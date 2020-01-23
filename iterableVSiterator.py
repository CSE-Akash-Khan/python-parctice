l = [1,2,3,4] #todo:-----------iterable
var = map(lambda a : a**2,l) #todo:-----iterator
#todo: iterabel:: first of all iterable call iter function and become iterator then call next function after and after
#todo: iterator:: its already iterator only call next function after and after and its return object. and only one time use for loop with this second time its dosem't work
#! EXAMPLE for iterabel:
# for i in l:
#     print(i)
#todo: what is happening behind the seen
# return_iter = iter(l) #now it is iterator
# print(return_iter) #its returned object
# print(next(return_iter)) 
# print(next(return_iter)) #todo: this way for loop work
# print(next(return_iter))
# print(next(return_iter))
# # print(next(return_iter)) #becouse l item has been ended
#! EXAMPLE for iterator
# for i in var:
#     print(i)
# #todo: we can use for loop only one time with this
# for j in var:
#     print(j)
#todo: what is happening behind the seen
# print(var) #its returned object
# print(next(var))
# print(next(var))
# print(next(var))
# print(next(var))
# # print(next(var)) #item has ended
