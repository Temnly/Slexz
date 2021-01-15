import shutil
def general():
 total, used, free = shutil.disk_usage("/")

 print(" ")
 print("Total: %d GB" % (total // (2**30)))
 print("Used: %d GB" % (used // (2**30)))
 print("Free: %d GB" % (free // (2**30)))
 print(" ")