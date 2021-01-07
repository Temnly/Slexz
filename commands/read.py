import os

def general():
 path = input("Type in the path of the .txt file you want to read -> ")
 f = open(path, 'r')
 file_contents = f.read()
 print (file_contents)
 f.close()
