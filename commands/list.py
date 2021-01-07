import os


def general():
 
 print(" ")
 print(" ")
 print("Type in the path you want to list")
 print(" ")
 print(" ")
 directory = input("Which directory do you want to list? ->  ")
 

 stuff = os.listdir(directory)
 print(stuff)