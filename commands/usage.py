import psutil
def general():
            print('CPU:', psutil.cpu_percent(), '%') 
            print('memory used:', psutil.virtual_memory()[2], '%')
