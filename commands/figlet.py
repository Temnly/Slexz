import pyfiglet

def general():
    print("Enter the text you want to make figlet of:")
    Input = input()
    figlet = pyfiglet.figlet_format(Input)
    print(figlet)
