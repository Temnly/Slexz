from ply import lex, yacc
from os import system
import os
import psutil
from time import gmtime, strftime
import subprocess
import requests
import sys
import threading
from tkinter import *

from importlib import import_module
from os.path import isfile, join, sep
from os import listdir







class MENU:
    def __init__(self):

      def clear():
       os.system('cls')
       print("PLEASE PRESS ENTER")
      def About():
        os.system("python menu/about_menu.py")
      def exit():
        root.quit()
        slexz = "python.exe"
        for proc in psutil.process_iter():
         if proc.name() == slexz:
            proc.kill() 

      root = Tk()
      #root.iconbitmap(default='p_icon.ico')
      width  = root.winfo_screenwidth()
      height = root.winfo_screenheight()
      root.geometry("{}x0".format(width, height))
      root.geometry("+{}+{}".format(0, 0))
      menu = Menu(root)
      root.config(menu=menu)
      filemenu = Menu(menu, tearoff=0)
      menu.add_cascade(label="File", menu=filemenu)
      filemenu.add_command(label="Clear", command=clear)
      filemenu.add_separator()
      filemenu.add_command(label="Exit", command=exit)

      helpmenu = Menu(menu, tearoff=0)
      menu.add_cascade(label="Help", menu=helpmenu)
      helpmenu.add_command(label="About...", command=About)




      mainloop()

class shell:
    def __init__(self):
        # Put whatever you wanted for the shell script.
      COMMANDS = dict()
      
      dir_path = f'.{sep}commands{sep}'
      all_commands = [f for f in listdir(dir_path) if isfile(join(dir_path, f)) and f != '__init__.py' and f.endswith('.py')]


      for cmd_file in all_commands:
        cmd = cmd_file.split('.')[0]
        module = import_module(f"commands.{cmd}")
        COMMANDS[cmd] = module.general


      while True:
        inp = input("Slexz -> ")
        if inp in COMMANDS.keys(): 
         COMMANDS[inp]()




Thread1 = threading.Thread(target=MENU)
Thread1.start()

Thread2 = threading.Thread(target=shell)
Thread2.start()
 

  
