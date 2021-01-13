import socket
def general():
    hostname = socket.gethostname() 
    IPAddr = socket.gethostbyname(hostname) 
    print(" ")
    print("Your Computer Name is: " + hostname) 
    print("Your Computer IP Address is: " + IPAddr) 
    print(" ")
