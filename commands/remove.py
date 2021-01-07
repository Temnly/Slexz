import os

def general():
 print(" ")
 print(" ")
 print("Type in the path of the File you want to delete")
 print(" ")
 print(" ")
 select = input("Which file do you want to remove? ->")
 os.remove(select)
 print("Removed Successfully")



