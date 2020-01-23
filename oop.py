
#? oop -- object orinted progrmming ---oop just a style/way to write code
#? class-- its represnt our object and explain what would be done our upcomming object
#? methode-- oop programming called methode insted of function
#! create a simple class
# class Person: #according to convenction class names first character always will be a capital latter
#     def __init__(self,first_name,last_name,age): #__init__ is a function or its called constractor and under bracker every thing called (attribute)
#         print("__init__ methode called")
#         self.first_name = first_name #self represent our object EX: p1.first name--its name can be anything
#         self.last_name = last_name #always attributes first item represent our object
#         self.age = age
# p1 = Person("Akash","Khan",20) #created object
# p2 = Person("Sohel","rana",22) #when we create object that time quickly call __init__ methode autometicly
# print(p1.first_name)
# print(p2.last_name)
#! Exercise 1
# class Laptop:
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name = brand_name #its called instance variable --and variable name can be anything
#         self.model_name = model_name
#         self.price = price
#         # self.full_specification = brand_name+" "+model_name+" "+price #todo: we can create extra instance variable
#         self.full_specification = f"brand:  {brand_name} , model:  {model_name} , price:  {price}"
# L1 = Laptop("apple","Mac book 15","75000")
# L2 = Laptop("Dell","dell 1275","45000")
# # print(f"brand:  {L1.brand_name} , model:  {L1.model_name} , price:  {L1.price}")
# print(L2.full_specification)

#! instance methode
#? instance r object same kotha/..ar class er under ee je sob function define kora hoy take methode bole
# class Person:
#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
#     def is_avobe(self):
#         return self.age>= 20

# p1 = Person("Akash", "khan",20)

# print(p1.full_name()) #todo instance methode
# print(p1.is_avobe())

#! Exercise 2
# class Laptop:
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name = brand_name #its called instance variable --and variable name can be anything
#         self.model_name = model_name
#         self.price = price
    
#     def discount(self,parcent):
#         store = (self.price*parcent)//100
#         return self.price - store

# L1 = Laptop("apple","Mac book 15",75000)
# L2 = Laptop("Dell","dell 1275",45000)
# print(L1.discount(10))

# #! class variable
# class Circle:
#     pi = 3.14 #TODO: class veriable--its can be use all methode under the class
#     def __init__(self,radius):
#         self.radius = radius
#         # self.pi = pi
#     def clc_area(self):
#         temp = 2*Circle.pi*self.radius
#         return format(temp,'.3f') #todo: its return 3 number after point
# c1 = Circle(3)
# print(c1.clc_area())

#.....................
# class Mobile:
#     apply_discount = 10 #todo: its called class variable
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#     def discount(self):
#         # off_price = (self.price*Mobile.apply_discount)/100 #todo: if you want to constant discount parcent then use class_name.class_variable
#         off_price = (self.price*self.apply_discount)/100 #todo: its changed some special product discount parcent and others product discount price will be same
#         return self.price - off_price

# Mobile.apply_discount = 20 #todo: changed discount parcent 10 to 20
# m1 = Mobile('realme','realme 2 pro',18000)
# m2 = Mobile('mi','mi note 7 pro',20000)
# m3 = Mobile('mi','mi note 8 pro',22000)

# m2.apply_discount = 50
# print(m1.discount(),m2.discount(),m3.discount())
# print(m2.__dict__) #todo: for showing details in my object

#! Excercise 3
# class Count:
#     counter = 0
#     def __init__(self):
#         # print('called init methode')
#         Count.counter += 1
# c1 = Count()
# c2 = Count()
# print(f"instance mehtode called {Count.counter} times")

#! class  methode
# class Person:
#     counter = 0
#     def __init__(self,first_name,last_name,age):
#         Person.counter += 1
#         self.first_name  = first_name
#         self.last_name = last_name
#         self.age = age
#     @classmethod
#     def cons_counter(cls): #todo: heres first argument class own
#         return f"you have created instance methode {cls.counter} times of {cls.__name__} class"
#     def is_avobe(self): #todo: heres first argumet instance
#         return self.age >= 20

# p1 = Person('akash','khan',20)
# p2 = Person('akash','khan',20)
# print(p1.is_avobe())
# print(Person.cons_counter()) #? same but its batter
# # print(p1.cons_counter()) #?same

#!real life example in class methode
# class Person:
#     counter = 0
#     def __init__(self,first_name,last_name,age):
#         Person.counter += 1
#         self.first_name  = first_name
#         self.last_name = last_name
#         self.age = age

#     def full_name(self):
#         return f"{self.first_name, self.last_name}"
#     @classmethod
#     def from_string(cls,string): 
#         first,last,age = string.split(',')
#         return cls(first,last,age) #heres created object
    
# # p2 = Person('akash','khan',20)
# p2 = Person.from_string('akash,khan,age') #we created object our own style
# print(p2.full_name())

#! static methode
# #? its work as a simple function
# class Phone:
#     def __init__(self,brand,model,price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#     def full_name(self):
#         return f"{self.brand} {self.model}"
#     @classmethod
#     def from_string(cls,string):
#         brand,model,price = string.split(',')
#         return cls(brand,model,price)
#     @staticmethod #? -------static mehtode-------
#     def static(): #todo: static methode
#         print('This is static mehtode')

# p1 = Phone.from_string('Nokia,1100,1500')
# print(p1.static())

#!  SOME IMPORTENT TOPICS
#? Encapsulation 
#? Abstraction
#? Some special naming convention
#? Name mangling

# class Phone:
#     def __init__(self,brand,model,price):   #| #?defination of encapsulation
#         self.brand = brand                  #|----instanace variable
#         self.model = model                  #|----Example: this is data
#         self.price = price                  #|
#     def make_a_call(self,phone_number):             #|performing this data with function
#         print(f"calling {phone_number}..........")  #|---and this is funciton
#     def full_name(slef):                            #| when we use data with methode under the class and same place
#         return f"{self.brand} {self.model}"         #|this callad encapsulation

# #?Abstraction
# #todo: Abstraction means -- hide of complexity---example
# l = [2,4,6,1]
# l.sort() #heres --l is a class and sort is methode of class--but heres hide all complexity of list class its clled abstarction
# print(l)

#? Some special naming convention
#todo:  _price : its means we have to use this as a private
#todo:  __price__ : its called dunder methode/magic methode
#todo: one thing keep minding -- python programing every thing is public -- nothing is private--example
# class Phone:
#     def __init__(self,brand,model,price):
#         self.brand = brand
#         self.model = model 
#         self._price = price # _price it's special naming convention. its means we should not change this instance variable and value

# phone1 = Phone('Nokia','1100',1500)
# print(phone1._price)
# phone1._price = -1500
# print(phone1._price) #amra change korte pari but korbona. developer eita dekhe bujbe its special eta change kora jabena

#? name mangling
# #todo: Name mangling we use , __name (not a convention)
# class Phone:
#     def __init__(self,brand,model,price):
#         self.brand = brand
#         self.model = model 
#         self.__price = price #its called name mangling

# phone1 = Phone('Nokia','1100',1500)
# # print(phone1.__price) #todo: output: AttributeError: 'Phone' object has no attribute '__price'.. whay showing this output lets see
# print(phone1.__dict__) #todo output:  '_Phone__price': 1500..python change __price to _Phone__price'
# print(phone1._Phone__price) #obj_name.class_name.instance_var/methode name--#? python eta change korar karon holo jano ei obj ta sudu ei class er jonno use hoy
# phone1._Phone__price = -1500
# print(phone1._Phone__price) #that means its not also prive -- its also a publc .. only python changed the name

