import os
import shutil
# print(os.getcwd()) #? it will show present directory

# os.mkdir('os_module')

# print(os.path.exists('os_module')) #? if alredy made this folder then return True else return false

#! best way for create folder
# if os.path.exists('movies'):
#     print('alredy exist')
# else:
#     os.mkdir('movies')

# open('file1.txt','a').close() #? for create a new file

#! for create a folder another location
# os.mkdir(r'G:\new_song') #?location path and folder name

#todo: another way--first changed directory then make folder
# os.chdir(r'G:') #? it will changed directory
# os.mkdir('new_song')
#todo: batter way for creating folder
# if os.path.exists(r'G:\new_song'):
#     print('alredy exist')
# else:
#     os.mkdir(r'G:\new_song')

#!......list directory...............................
# print(os.listdir()) #? it will given list of this directorys file and folder
# print(os.listdir(r'G:')) #? for showing another directories list
#todo: another way change_directory before like this

#!for getting path directorys files and folders -- heres 2 way getting path

#? 1). its never shouldn't does
# for item in os.listdir():
#     print(r"C:\Users\Dell\Desktop" + "\\" + item)

#? 2). its a best way it's should do 
# for item in os.listdir():
    # print(os.path.join(os.getcwd(),item))
    # print(f"{os.getcwd()}\{item}")
    # print(os.getcwd()+'\\'+item)
    #todo: every way is right

#!........................................................
#? for showing directories all file and folder..and all directorys and files under directory
# os.chdir(r'G:\os_module')
# # print(os.listdir())
# iterator = os.walk(r'G:\os_module') #?it will return generator object. and this generator completed 3 yeild one time and its return 3 item 1.current_path 2.)folder_name 3.)file_name
# for current_path, folder_name, file_name in iterator:
#     print(f'current path {current_path}')
#     print(f'folder name {folder_name}')
#     print(f'file name {file_name}')

#! ...........some more os module.........................
# os.chdir('G:\os_module')
# os.rmdir('song') #? it's remove only empty folder

# os.makedirs('new/movies/song') #? its can make folder under folder

#! shutil module---tuto: 229
# os.chdir('G:\os_module')
# shutil.rmtree('new') # ?one thing mind that its not sotre recile bin its deleted parmanently
os.chdir('G:\os_module\document')

# shutil.copy('file1.txt','new_file/file1.txt')#?for copying file

# shutil.move('file2.txt','new_file/file.txt') #?for moving file

shutil.move('new_file','new_text/new_file') #?for foving folder


#!.....................................All os command........................................................
#todo..................................all shutil command....................................................

#! os command
#? import os
# os.getcwd()  #? getting current working directory
# os.mkdir('os_module') #? creating folder
# os.mkdir(r'G:\new_song') #?for creating folder another location
# os.path.exists('folder/file name') #? if alredy made this folder then return True else return false
# open('file1.txt','a').close() #? for create a new file
# os.chdir(r'G:') #? it will changed directory
# print(os.listdir()) #? it will given list of this directorys file and folder
# print(os.listdir(r'G:')) #? for showing another directories list
# os.walk(r'G:\os_module') #?it will return generator object. and this generator completed 3 yeild one time and its return 3 item 1.current_path 2.)folder_name 3.)file_name
# os.rmdir('song') #? it's remove only empty folder. it's not enough for us
# os.makedirs('new/movies/song') #? its can make folder under folder

#! shutil module
#? import shutil
# shutil.rmtree('new') # ?one thing keep in mind that its not sotre reycle bin its deleted parmanently it's batter then rmdir
# shutil.copy('file1.txt','new_file/file1.txt')#?for copying file 
# shutil.move('file2.txt','new_file/file.txt') #?for moving file--moving_file_name|keeping_folder_name|again file name
# shutil.move('new_file','new_text/new_file') #?same way