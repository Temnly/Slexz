import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os
 
# FME variables.
import fme
status = fme.status
errorMsg = fme.failureMessage
logFile = fme.logFileName
 
# E-mail message values.
subject = "FME Translation FAILURE"
to = "receiver@domain.com"
sender = "Your FME script <sender@domain.com>"
text = "FME translation failed with error message: " + errorMsg + \
"\r\n\r\nSee attached logfile for details."
 

# Credentials.
AUTHREQUIRED = 0
username = "smtp.user@domain.com"
password = "smtppassword"
smtpServer = "smtp.server.com"
 

# Create and return a message with a logfile attachment.
def createMessage():
# Set up the e-mail.
message = MIMEMultipart()
message["Subject"] = subject
message["To"] = to
message["From"] = sender
message["Date"] = formatdate(localtime=True)
message.attach(MIMEText(text))
 
# Attach the logfile.
attachment = MIMEBase("application", "octet-stream")
attachment.set_payload(open(logFile, "rb").read())
Encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition",
'attachment; filename="%s"' % os.path.basename(logFile))
message.attach(attachment)
return message
 
# Send the passed in message.
def sendMessage(message):
server = smtplib.SMTP(smtpServer)
if AUTHREQUIRED:
server.login(username, password)
server.sendmail(sender, to, message.as_string())
server.quit()
 
# E-mails the translation results on failure.
def mailResults():
if status == 0:
message = createMessage()
sendMessage(message)
 
# Call function for FME to execute.
mailResults()
