while True:

    choice = input("Slexz -> ")

    if choice in ('version', 'help', 'easteregg', 'pingit', 'clearit', 'usage', 'exit'):

        if choice == 'version':
            print(" ")
            print(" ")
            print(" ")
            print("--------------------")
            print("       Slexz")
            print("    Version 1.0")
            print("--------------------")
            print(" ")
            print(" ")
            print(" ")

        elif choice == 'help':
            print(" ")
            print("--------------------")
            print("Available Commands:")
            print(" ")
            print("help - show all commands")
            print("version - show the version of Slexz")
            print("pingit - ping a site")
            print("clearit - clear the shell")
            print("usage - show the usage of your pc")
            print("exit - exit Slexz")
            print("--------------------")
            print(" ")

        elif choice == 'easteregg':
            print("uh you really found that?")



        elif choice == 'pingit':
         
            url = input('Enter URL: ')
            system("ping " + url)

        elif choice == 'clearit':
            os.system('cls')  
            os.system('clear')  

        elif choice == 'usage':

            print('CPU:', psutil.cpu_percent(), '%') 
            print('memory used:', psutil.virtual_memory()[2], '%')

        elif choice == 'exit':
            exit()


                           
    else:
        print("$error")
