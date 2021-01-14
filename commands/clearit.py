import os
import sys
def general():
  platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
  if sys.platform not in platforms:
      return sys.platform
    
  operatingsystem = platforms[sys.platform]
  print(operatingsystem)
  if operatingsystem=="Windows":
    os.system('cls')
  else:
    os.system('clear')
  # os.system('clear')