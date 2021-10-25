import time
import os
from os import path
textpath = "data.bat"
standartpath = '\Program'
version = 1.1
os.system("color b")
z = 0
name = path.exists("activateStatus.txt")
if name == True:
  g = open("activateStatus.txt" , "r")
  activate = bool(g)
else:
  activate = False
dir = path.exists("additions\dirStatus.txt")
if dir == True:
  gf = open("additions\dirStatus.txt", "r")
  showdirsandfiles = bool(gf.read().strip())
else:
  showdirsandfiles = False
activate
f12 = True
userdataFileName = "userdata.txt"
activateNumbers = [
  "7590451472334898",
  "1337247268576815",
  "5271583690585701",
  "3224933122273952",
  "6297455581955869",
  "7328351253767243",
  "6749230326637358",
  "2240581722397084",
  "1149124061405841",
  "2744411029677893"]
def processLogin():
  os.system('cls' if os.name == 'nt' else 'clear')
  a = False
  while a == False:
    print("Enter the username")
    command = input("$ ")
    if(command == USER):
      print("enter the password")
      command = input("$ ")
      if(command == PASSWORD):
        print("All right!You have successfully logged in to the system")
        a = True
        isLoggedIn = True
      else:
        print("the password is incorrect")
        a = False
        

name = path.exists(userdataFileName)
if(name == True):
  g = open(userdataFileName,'r')
  lines = g.readlines()
  if (len(lines) >= 1):
    USER = lines[0].strip()
  if (len(lines) >= 2):
    PASSWORD = lines[1].strip()
    
  g.close()
  isLoggedIn = False
  processLogin()
  b = False
else:
  b = True

  while b == True:
    print("Введи своё имя")
    USER = input("$ ")
    g = open(userdataFileName,'w')
    g.write(USER)
    g.close()
    print("Введи свой пароль")
    PASSWORD = input("$ ")
    l = open(userdataFileName,'a')
    l.write("\n" + PASSWORD)
    l.close()
    b = False
print("EvoOs version "+ str(version) + " User - " + USER + ". используй команду help для получения информации о командах ")
print("EvoOs inc. 2021-2025 гг.")

isLoggedIn = True
version = 1.1
while True:
  command = input(os.getcwd() + "$ ").split()
  if(command[0] == "dir" and showdirsandfiles == True):
    if (len(command) < 2):
      print(os.listdir(os.getcwd()))
    else:
      print(os.listdir(command[1]))
  if(command[0] == "activatestatus"):
    print(activate)
  if(command[0] == "setvalue"):
      if (command[1] == "user"):
        USER = command[2]
        g = open(userdataFileName,'w')
        g.write(USER + "\n" + PASSWORD)
        g.close()
      if (command[1] == "password"):
        PASSWORD = command[2]
        g = open(userdataFileName,'w')
        g.write(USER + "\n" + PASSWORD)
        g.close()
  if(command[0] == "version"):
    print(version)
  if(command[0] == "shutdown"):
    print("shutdown")
    time.sleep(5.5)
    quit()
  if(command[0] == "function.enable" and activate == True):
    if(command[1] == "showdirsandfiles"):
      showdirsandfiles = True
      x = open("additions\dirStatus.txt" , "w")
      x.write(str(showdirsandfiles))
      x.close()
    else:
      print("now additions with this name")
    if(command[0] == "disable" and activate == True):
      if(command[1] == "files"):
        showdirsandfiles = False
        x = open("additions\dirStatus.txt" , "w")
        x.write(str(showdirsandfiles))
        x.close()
        print("Success!")
      else:
        print("now additions with this name")
  if(command[0] == "cd" and showdirsandfiles == True):
    if (command[1].find(":") == 1):
      nowlocation = os.getcwd()
      nowlocation = command[1]
      os.chdir(command[1])
    else:
      nowlocation = os.getcwd()
      kx = nowlocation + command[1]
      os.chdir(kx)
      nowlocation = kx

  if(command[0] == "weather"):
    os.startfile("Weather.exe")
  if(command[0] == "Status"):
    print(str(showdirsandfiles))
  if(command[0] == "texteditor" and showdirsandfiles == True):
    os.startfile(textpath)
  if(command[0] == "mkdir" and showdirsandfiles == True):
    os.mkdir(command[1])
  if(command[0] == "removedir" and showdirsandfiles == True):
    os.rmdir(command[1])
  if(command[0] == "removefile" and showdirsandfiles == True):
    os.remove(command[1])
  if(command[0] == "rename" and showdirsandfiles == True):
    os.rename(command[1], command[2])
  if(command[0] == "calc"):
    os.startfile("calc.exe")
  if(command[0] == "snake"):
    os.startfile("game2.exe")
  if(command[0] == "cls"):
    os.system('cls' if os.name == 'nt' else 'clear')
  if(command[0] == "game"):
    os.startfile("game.exe")
  if(command[0] == "start" and showdirsandfiles == True):
    cmdline = "start " + command[1]
    cmdindex = 1
    while (cmdindex < len(command)):
      cmdindex = cmdindex + 1
      cmdline = cmdline + " " + command[cmdindex]
    
    os.system(cmdline)
  if(command[0] == "help"):
    text = open('help.txt','r')
    print(*text)
    text.close()
  if(command[0] == "name"):
    print("Your name is " + USER)
  if(command == "logout" and isLoggedIn == True):
    print("logout")
    isLoggedIn = False
  if(command == "logon" and isLoggedIn == False):
    processLogin()
  if(command == "password"):
    print("Your password is " + PASSWORD)
  if(command  == "activate" and activate == False):
    while f12 == True:
      print("you need activate the system. Please enter the activation code")
      command = input("Activation code - ")
      if (activateNumbers.index(command) >= 0):
        activate = True
        print("The system has been successfully activated")
        f12 = False
      else:
        print("Invalid activation key")
        f12 = True
