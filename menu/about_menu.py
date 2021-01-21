from tkinter import *


root = Tk()
root.resizable(False, False)
window_height = 500
window_width = 900

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

l = Label(root,text="About", font="Arial 50")

l.pack()

space = Label(root,text=" ", font="Arial 18")
space.pack()

l1 = Label(root,text="Version", font="Arial 25")

l1.pack()

l2 = Label(root,text="1.2", font="Arial 17")

l2.pack()

root.mainloop()
