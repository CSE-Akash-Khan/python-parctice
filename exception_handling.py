
#! Try ,except
#! else , finally
#? tutorial = 207,208
# while True: #jotokhon porjonto sotto na hoy totokhon porjont except block cholte thakbe
#     try:
#         age = int(input("Enter your age: "))
#         break #?sotto hole loop break hoye jabe
#     except ValueError: #?jodi amra guess korte pari je ai error aste pare and ai error jodi hoy ta hole ai block cholbe
#         print("mybe you entered string insted of number try again!")
#     except: #? try er multiple block hote pare
#         print('Invalid input')

# if age < 18:
#     print("you can't play this game")
# else:
#     print("you can play this game")

#! else finally with try except
# while True:
#     try:
#         user = int(input("Enter a number: "))
#     except ValueError:
#         print("mybe you entered string insted of number try again!")
#     except:
#         print('Invalid input')
#     else: #?only when try block will be True then its run
#         print(f"you entered = {user}")
#         break
#     finally: #todo: its always run
#         print("finally blocks..........")

#! exercise
# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "dont divide by zero"
#     except TypeError:
#         return "please input number only"

# print(divide(25,5))
# print(divide(25,0))
# print(divide('25',5))
#! exercise.. return dufult error.......
# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as error: #? by this will be printed by difult error
#         return error
#     except TypeError as err: #?after as you can write anything
        # return err #!or
        # print('you have to enter a number')

# print(divide(25,5))
# print(divide(25,0))
# print(divide('25',5))
#! custom exception
# class NameTooshortError(ValueError):
#     pass
# def validate(name):
#     if len(name) < 8:
#         raise NameTooshortError('your name is too short') #we can raise error as my way. for this you have to define a class before start
#     return f"hello...{name}"

# user = input("Enter your name: ")
# print(validate(user))
# # print(f'hello...{user}')
