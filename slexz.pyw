from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import families, Font
from PIL import ImageTk
from PIL import Image
import os
import sys
import psutil
import datetime
import shutil
import time
import socket
import platform
from datetime import datetime
import subprocess

root = Tk()
root.geometry("700x360")
root.resizable(0, 0)
root.title("Slexz")

def clear():
 Output_Box.delete('1.0', END)
def About():
 #about
 os.system("python menu/about_menu.pyw")
def exit():
 #exit
 root.quit()
def newtab():
 #It's not working right now! It's much to deal with, so we focus on it later
 print("Not working right now!")
def documentation():
 path = "documentation"
 path = os.path.realpath(path)
 os.startfile(path)

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Clear", command=clear)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)

New = Menu(menu, tearoff=0)
menu.add_cascade(label="New", menu=New)
New.add_command(label="New Tab", command=newtab)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Documentation", command=documentation)
helpmenu.add_separator()
helpmenu.add_command(label="About", command=About)


def check_input(event):
    inp = Input_Entry.get()
    Input_Entry.delete(0, END)

    if inp == 'date':
     now = datetime.datetime.now()
     message = now.strftime("%d-%m-%Y")

    elif inp == 'easteregg':
        message = "uh you really found that?"

    elif inp == 'inet':
     hostname = socket.gethostname() 
     IPAddr = socket.gethostbyname(hostname) 
       
     message = "Your Computer Name is: " + hostname + "\nYour Computer IP Address is: " + IPAddr
    
    elif inp == 'info':
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        uname = platform.uname()
        message = "="*20 + "System Information" + "="*20 + f"\nSystem: {uname.system}" + f"\nNode Name: {uname.node}" + f"\nRelease: {uname.release}" + f"\nVersion: {uname.version}" + f"\nMachine: {uname.machine}" + f"\nProcessor: {uname.processor}\n" + "="*20 + "Boot Time" + "="*20 + f"\nBoot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n" + "="*20 + "CPU Info" + "="*20 + "\nCPU Usage Per Core:" + f"\nTotal CPU Usage: {psutil.cpu_percent()}%\n"
    elif inp == 'logout':
        os.system("shutdown -l")
    elif inp == 'new -e':
        os.system('notepad.exe')
    elif inp == 'new -s':
        subprocess.call('start /wait python slexz.py', shell=True)
    elif inp == 'shutdown':
        os.system("shutdown /s")
    elif inp == 'space':
       total, used, free = shutil.disk_usage("/")
       message = "Total: %d GB" % (total // (2**30)) + "\nUsed: %d GB" % (used // (2**30)) + "\nFree: %d GB" % (free // (2**30))
    elif inp == 'time':
      now = time.localtime()
      message = time.strftime("%H:%M", now)
    elif inp == 'version':
            message = "\n\n--------------------\n       Slexz\n    Version 1.1\n--------------------\n\n"
            print(" ")
            print("--------------------")
            print("       Slexz")
            print("    Version 1.2")
            print("--------------------")
            print(" ")
            print(" ")

    elif inp == 'exit':
        exit()


    else:
        message = 'This command is not available'

 
    Output_Box.configure(state="normal")
    Output_Box.insert(END, '{}\n'.format(message))
    Output_Box.configure(state="disabled")









Output_Box = Text(root)
Output_Box.pack(fill=X)
Output_Box.configure(foreground="#000000", takefocus="", cursor="ibeam", state="disabled", height=21)

Input_Entry = Entry(root)
Input_Entry.focus()
Input_Entry.pack(fill=X, side=BOTTOM)
Input_Entry.configure(foreground="#000000", takefocus="", cursor="ibeam")



root.bind('<Return>', check_input)

root.mainloop()
