from ply import lex, yacc
from os import system
import os
import psutil
from time import gmtime, strftime
import subprocess
import requests

from importlib import import_module
from os.path import isfile, join
from os import listdir


COMMANDS = dict()

dir_path = './commands'
all_commands = [f for f in listdir(dir_path) if isfile(join(dir_path, f)) and f != '__init__.py' and f.endswith('.py')]


for cmd_file in all_commands:
  cmd = cmd_file.split('.')[0]
  module = import_module(f"commands.{cmd}")
  COMMANDS[cmd] = module.general


while True:
  inp = input("Slexz -> ")
  if inp in COMMANDS.keys(): 
    COMMANDS[inp]()
