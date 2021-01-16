import psutil
def general():
 battery = psutil.sensors_battery()

 percent = str(battery.percent)
 print(percent+'%')