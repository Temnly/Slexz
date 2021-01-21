from os import system

def general():


 with open("etc/settings/language.txt", "r") as f:
      text = f.read().strip()


 if text == "en":
      url = input('Enter URL: ')
      system("ping " + url)
 elif text == "de":
      url = input('Gebe deine gewünschte URL ein: ')
      system("ping " + url)
 else:
    print("Error. Unsupported Language!")