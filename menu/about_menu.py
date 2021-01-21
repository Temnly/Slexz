from tkinter import *
from tkhtmlview import HTMLLabel

root = Tk()
root.resizable(False, False)
window_height = 500
window_width = 900

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
HTMLLabel(root, html='<h2 style="text-align: center;">About</h2><p style="text-align: center;">Version <br>1.2</p><br><p style="text-align: center;">Build ID<br>Not available</p>').pack()



root.mainloop()