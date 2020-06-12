import smtplib,ssl

sender_mail = 'shrivastwavivek44@gmail.com'
receivers_mail = ['shrivastwavivek44@gmail.com']
port = 465

smtp_server = "smtp.gmail.com"
password = "J3JDY52vivek";

message = """From: From Person %s 
To: To Person %s 
Subject: Sending SMTP e-mail  
This is a test e-mail message. 
hey i am successed in penitrating into the email through the python...
looks like python is a great app to do such things....
"""%(sender_mail,receivers_mail)


server  = smtplib.SMTP_SSL(smtp_server,port)
server.login(sender_mail,password)
server.sendmail(sender_mail, receivers_mail, message)
server.quit()
print("Successfully sent email")
