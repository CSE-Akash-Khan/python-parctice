
#! property gatter and setter
# class Mobile:
#     def __init__(self,brand,model,price):
#         self.brand = brand
#         self.model = model
#         self._price = max(price,0)
#         # self.full_specification = f"{self.brand} {self.model} and price {self._price}" #? heres a problem--jokhon amra pore kono value change kori tokhon eita change hoy na
#     @property #?property decorator use korle methode ke function er moto call korar dorkar nay..as attribute er  moto call korte parbo
#     def full_specification(self):
#         return f"{self.brand} {self.model} and price {self._price}"

#     #? getter #setter
#     #gatter mane property decorator and setter mane setter decorator --sobsomoy gatter er por setter define korte hobe na hole error dekhabe
#     @property #todo:--its gatter
#     def price(self):
#         return self._price

#     @price.setter #? setter decorator
#     def price(self,new_price):
#         self._price = max(new_price,0)

# m1 = Mobile('Realme','realme 2 pro',1000)
# # print(m1.brand)
# # print(m1.model)
# m1.price = -500
# print(m1.price)
# print(m1.full_specification)

#! inheritance
#! multilevel inheritance
#! Methode overriding
#! isinstance , issubclass
# class Phone: #todo: base class
#     def __init__(self,brand,model,price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def make_a_call(self,number):
#         return f"calling {number}........"
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"


# class Smart_phone(Phone): #todo: inherit Phone class----child class/drive class
#     def __init__(self,brand,model,price,ram,memory_rom,battery_ampier):
#         # Phone.__init__(self,brand,model,price) #less use full
#         super().__init__(brand,model,price) #more usefull
#         self.ram = ram
#         self.memory_rom = memory_rom
#         self.battery_ampier = battery_ampier

#     def full_name(self): #
#         return f"{self.brand} {self.model} and price is {self.price}"

# #? can we drive more then one class from drive calss---yes
# class Smart_phone2(Phone): #todo: inherit phone class
#     def __init__(self,brand,model,price,ram,memory_rom,battery_ampier):
#         super().__init__(brand,model,price)
#         self.ram = ram
#         self.memory_rom = memory_rom
#         self.battery_ampier = battery_ampier

# #? Multi level inheritance
# class flagship_phone(Smart_phone):
#     def __init__(self,brand,model,price,ram,memory_rom,battery_ampier,snap_dragon):
#         super().__init__(brand,model,price,ram,memory_rom,battery_ampier)
#         self.snap_dragon = snap_dragon

# p1 = Phone('Nokia','1100',1500)
# sm = Smart_phone('redmi','redmi note 7',20000,'4gb','64 gb',4000)
# sm2 = Smart_phone2('redmi','redmi note 7',20000,'4gb','64 gb',4000) #inheritance
# realme2_pro = flagship_phone('realme','realme_2_pro',20000,'4gb','64 gb',4000,665) #multi level inheritance
# #? methode over loading
# # print(realme2_pro.full_name())
# # print(sm.full_name())
# #? MRO -- Methode regulation order
# # help(realme2_pro) #help not running this directory its will run another directory
# #? isinstance
# print(isinstance(sm,Smart_phone)) # its checked that sm instance is from smart_phone class---ans: yes -- true
# print(isinstance(sm2,Smart_phone)) # its checked that sm instance is from smart_phone class---ans: No -- false
# #? issubclass
# print(issubclass(flagship_phone,Smart_phone)) #its checked that flagship_phone class is subclass form smartphone class -- ans: Yes--true
# print(issubclass(flagship_phone,Smart_phone2)) #its checked that flagship_phone class is subclass form smartphone class -- ans: No--flase

#! multiple class -- actually its useless

# class A:
#     def calling_a_class(self):
#         return "I'm just class A"
#     def hello(self):
#         return "hello i am under the class A"

# class B:
#     def calling_a_class(self):
#         return "I'm just class B"
#     def hello(self):
#         return "hello i am under the class B"

# class C(A,B):
# # class C(B,A):
#     pass

# c1 = C()
# b1 = B()
# print(c1.hello())
# # help(c1) #? we show by this methode regulation order MRO
# print(C.mro()) #? This another way for showing --- Its return list
# print(C.__mro__) #? Both are same its return Tuple

#todo.................................................................................

#! Dunder methode
#! Operator overriding
#! polymorphisom

# class Phone: #todo: base class
#     def __init__(self,brand,model,price):
#         self.brand = brand
#         self.model = model
#         self.price = price
    
#     def phone_name(self):
#         return f"{self.brand} {self.model}"

    #? str , repr
#     def __str__(self): # its use user
#         return f"{self.brand} {self.model}"
#    #if we difine both always call __str__ methode 

#     def __repr__(self): #its use developer becouse latter they can debug -- we can create object by this methode
#         return f"Phone(\'{self.brand}\',\'{self.model}\',{self.price})"
    # def __len__(self):
    #     return len(self.phone_name())

#     #! Operator over loading--
#     # ?we are using many operator with one object--its called operator over loading
#     def __add__(self,other):
#         return self.price + other.price

#     def __mul__(self,other):
#         return self.price * other.price
#     #? we can over load many operator check this web site::- docs.python.org

#     #! polymorphisom
#     #? that means -- many forms -- any things many form Example:
#     # 2 + 3 = 5 #?ekhane + use kore amra duiti sonkha jog koresi
#     #'akash' + 'Khan' = akashkhan #? ekhane + use kore duiti string ke add koresi
#     #that means ekta operator ke onek vabe use korte partesi. that means ekta jiniser ekadik rup/form etakey muloto bole polymorphisom
#     #? another example:
#     l = [1,3,4]
#     t = (1,2,3)
#     s = "abc"
#     len(l)
#     len(t)
#     len(s)
#     #ekhane amra len function ke list tuple string onek datatype er sathe use korte partesi that means ekoy len function ke onek vabe use korte partesi etay polymorphisom
#     #? operator over loadin or methode over loading oo polymorphisom er example hisebe bola jay

# class Smart_phone(Phone): #todo: inherit Phone class----child class/drive class
#     def __init__(self,brand,model,price,ram,memory_rom,battery_ampier):
#         # Phone.__init__(self,brand,model,price) #less use full
#         super().__init__(brand,model,price) #more usefull
#         self.ram = ram
#         self.memory_rom = memory_rom
#         self.battery_ampier = battery_ampier

#     def phone_name(self): #
#         return f"{self.brand} {self.model} and price is {self.price}"



# #? Object
# my_phone = Phone('Nokia','1100',1500)
# my_phone2 = Phone('Nokia','1100',1500)
# print(my_phone + my_phone2)
# print(my_phone * my_phone2)

# l = [1,3,4]
# print(l) #its return our list full fill
# print(my_phone) # its return memory location op:<__main__.Phone object at 0x00FCFBD0>-- solve this problem we have to create dunder methode

# print(my_phone.__str__()) #i think its batter way
# print(repr(my_phone)) # we can call our methode both way
# print(len(my_phone))
# print(my_phone.__len__())

# #? polymorphisom
# my_phone = Phone('Nokia','1100',1500)
# print(my_phone.phone_name) 

# sm_phone = Smart_phone('redmi','redmi note 7',20000,'4gb','64 gb',4000)
# print(sm_phone.phone_name())
# ekhane phone class ee phone name methode and smart_phone class phone name methode use korte partesi etay muloto polymorphisom

#todo................................................................................
'''important tutorial::--
 tutorial no -- 197
 tutorial no -- 198
 '''
