import subprocess as sp
import os

def general():
	print(" ")
	print(" ")
	print("    Here is a list of what you can setup")
	print("=============================================")
	print(" ")
	print("1. Change Language")
	print(" ")
	print(" ")
	inp = input(">>> ")


	if inp == '1':
		print(" ")
		print(" ")
		print("   Change Language   ")
		print("=====================")
		print(" ")
		print(" ")
		print("NOTE: Your Text Editor is opening now. Below is a list for available languages")
		print(" ")
		print("English = en")
		print("German = de")
		print(" ")
		print(" ")
		programName = "notepad.exe"
		fileName = "etc/settings/language.txt"
		sp.Popen([programName, fileName])
	else: 
		exit()