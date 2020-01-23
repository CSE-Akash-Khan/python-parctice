
#? tutorial :-- 212

#todo: its have to run out site to this folder

#! Why dibugging
#? we use dibugger for searching our error. by this we can execute our code line by line and catch our error. some time we face error and thuse type of output we want. but we dont get our exceptable out put .for solving this problem we can use dibugger.its execute and run our code line by line lets see.....
#! steps for dibugging
#? 1). set trace
#? 2). execute code line by line

import pdb #todo: for dibugging we have to import pdb module
#defanation of module: module wroted by python file contains, usefull class,and function.when we import module we can use every thing which wroted under the module.

pdb.set_trace()
name = input('Type your name: ')
age = input('Type your age: ')
# pdb.set_trace() #?it's we can use any place. jekhane eta likbo sekhan theke eta dibagging start korbe
print(f"your name is {name} and age is {age}")
age2 = age + 5 #i make this fault as i known
print(f"you will be {age2} in next 5 years")

#! dibugging command
#? l -- show which line now executing
#? n -- run executing line
#? c -- continue program (pressing c program will be run)
#? q -- its use for close dibugging
