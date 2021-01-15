import datetime

def general():
 now = datetime.datetime.now()
 print("DD-MM-YYYY")
 print(now.strftime("%d-%m-%Y"))
