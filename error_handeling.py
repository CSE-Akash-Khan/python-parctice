
# #! raise errror
# def add(a,b):
#     if type(a) is int and type(b) is int:
#         return a+b
#     raise TypeError('opps you pass wrong input') #we use raise for showing error
# print(add('akash','khan'))

#!raise error example 
#! NotImplementedError
#! abstract methode - from java
#? tutorial :-- 205
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def sound(self): #its called abstract methode.actually pythons has not abstract methode this methodes java language called abstract methode
#         raise NotImplementedError("this methode you have to define uder the subclass")

# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def sound(self):
#         return "bhow bhow"

# class Cat(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def sound(self):
#         return "mu mu"

# a1 = Animal('dog')
# # print(a1.sound())
# d1 = Dog('boony','pet')
# # print(d1.sound())
# c1 = Cat('pisu','posa')
# print(c1.sound())

#! raise error example 2
class Mobile:
    def __init__(self,name):
        self.name = name

class Mobile_store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            return self.mobiles.append(new_mobile)
        raise TypeError('your insatance should be a mobile class')

one_plus = Mobile('one plus 8')
one_plus2 = Mobile('one plus 7')
smasung = "smasung galaxy not 10"
mobostore = Mobile_store()

mobostore.add_mobile(one_plus) #? one plus object ti append hoyse self.mobile variable er modde
# print(mobostore.mobiles) #?output: [<__main__.Mobile object at 0x02DFFE90> eta object return kore
self_mobiles = mobostore.mobiles #? ekhane self.mobiles = [one_plus] roise.one plus nijey ekta mobile class er instance tai eti object return kore
print(self_mobiles[0].name) #? er imagenary figur holo--(one_plus.name)-- list er 0 number position ee ase one_plus([0] = oneplus). r eti mobile class er object. tai muloto mobile class er name dekha hoyse.