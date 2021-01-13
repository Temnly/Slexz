import os


def general():
 
 with open("etc/settings/language.txt", "r") as f:
      text = f.read().strip()
 if text == "en":
      print(" ")
      print(" ")
      print("Type in the path you want to list")
      print(" ")
      print(" ")
      directory = input("Which directory do you want to list? ->  ")
 elif text == "de":
      print(" ")
      print(" ")
      print("Gebe den Pfad ein, den du auflisten möchtest")
      print(" ")
      print(" ")
      directory = input("Welchen Ordner möchtest du auflisten lassen? ->  ")
 else:
    print("Error. Unsupported Language!")

 stuff = os.listdir(directory)
 print(stuff)


