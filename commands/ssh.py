import paramiko 

def general():
 #input
 host = input("Hostname -> ")

 port = input("Port -> ")

 username = input("Username -> ")

 password = input("Password -> ")

 while True:
  command = input("SSH -> ")


 ssh = paramiko.SSHClient()

 ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

 ssh.connect(host, port, username, password)


 stdin, stdout, stderr = ssh.exec_command(command)

 lines = stdout.readlines()

 print(lines)