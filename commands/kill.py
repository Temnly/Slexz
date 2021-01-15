import psutil

def general():

 inp = input("Kill -> ")

 for proc in psutil.process_iter():
    if proc.name() == inp:
        proc.kill()