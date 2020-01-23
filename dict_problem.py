# def cube_finder(number):
#     total = {}
#     for i in range(1,number+1):
#         total[i] = i**3
#     return total
# print(cube_finder(6))
#! exercise 2
user = {}
name = input("Enter your name: ")
age = input("Enter your age: ")
fav_move = input("Enter your favorite movie: ").split(",")
fav_song = input("Enter your fav song: ").split(",")

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_move
user['fav_song'] = fav_song
# print(user)
for key,value in user.items():
    print(f"{key} : {value}")