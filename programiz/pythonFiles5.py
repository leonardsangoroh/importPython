#python directory and files management

#get current directory
import os

print(os.getcwd())

#change directory
os.chdir('Users/leesangoroh')

#list directories and files in python

#lists all subdirectories
os.listdir()

os.listdir('Users/leesangoroh')

#make directory
os.mkdir('test')

#rename a directory
os.rename('test','newOne')

#remove directory or file
os.remove('newOne.txt')

#remove directory
os.rmdir('newOne')

# remove dir using the shutil module
import shutil

shutil.rmtree('mydir')