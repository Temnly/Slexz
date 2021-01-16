import psutil

def general():
  slexz = "python.exe"

  for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == slexz:
        proc.kill()