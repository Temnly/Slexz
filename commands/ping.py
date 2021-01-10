from os import system

def general():


 with open("etc/settings/language.txt", "r") as f:
      text = f.read().strip()

 #English Language
 if text == "en":
      url = input('Enter URL: ')
      system("ping " + url)
 #German Language
 elif text == "de":
      url = input('Gebe deine gewünschte URL ein: ')
      system("ping " + url)
 else:
    print("Error. Unsupported Language!")
