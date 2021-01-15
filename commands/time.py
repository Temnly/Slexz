import time

def general():
 now = time.localtime()
 my_time = time.strftime("%H:%M", now)
 print("HH:MM")
 print(my_time)
