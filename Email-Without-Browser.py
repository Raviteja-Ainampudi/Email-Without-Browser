# -*- coding: utf-8 -*-
"""
Created on Sun Jul 03 13:14:27 2016

@author: RAVI TEJA
"""
#!/usr/bin/python

#The basic intention of this script is to send an email to a user without using a browser on host machine.

#As the reputed email providers like Gmail and Yahoo have blocked the external access of SMTP servers without a browser.
#In order to access the SMTP server of both Gmail and Yahoomail. We need to turn ON the "ACCESS FOR LESS SECURE APPS"
#Send email from GMAIL and Yahoomail without a browser.

#In Gmail - To Turn ON - Access for less secure apps - use this - https://www.google.com/settings/security/lesssecureapps
#In Yahoomail - To Turn ON - Access for less secure apps - use this - https://login.yahoo.com/account/security?
#You can revoke the changes once done using this python script

import smtplib

From = '<your-email address>' #It could be either your gmail or yahoomail address  
Recipient  = '<reciever-email address>'  #Email address to which email has to be sent

#Make sure you use right email address at the right place
#Message body of the email (It was designed in HTML)
Messege = """From: YOUR-NAME <your-email address > 
To: RECIEVER-NAME <reciever-email address>
MIME-Version: 1.0
Content-type: text/html
Content-encoding: gzip
Subject: Testing a SMTP e-mail using HTML script

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>Hello there!! </h1>
<h2 style = "color:blue;"> You have recieved this email by using a Python script. </h2>
<h3 style = "color:#A43118;"> Learn Python. Have fun </h3>
<h4 style = "font-family:Verdana;"> Learn+Live+Love = Life </h4>
<p> <b> <font face="Monaco" color="green"> Thanks for using my code. </font> </b> </p> 

<img src = "https://pbs.twimg.com/profile_images/431119224317026304/IA5vDLzt.jpeg" alt = "Spartan Image" width="100" height="100"> </img>
<p> Spartans Never Give Up.... Hoooooo ! </p>
"""  

# Authenication Credentials
username = 'YOUR-EMAIL-ADDRESS' #It could be either a gmail or yahoo mail address  
password = 'YOUR-EMAIL-PASSWORD' #Password of above email for login purpose at Mail Exhange Server.(No Worries). It is safe until your IDE and PC are safe. 
  
# mail is being sent :  
  
#Any mail exhange servers could be used from gmail and yahoomail. Make sure you comment out the redundant one (server)
#To establish connection to the SMTP Server
  
server = smtplib.SMTP('smtp.mail.yahoo.com:587')  #587 is a Mail submission port
#server = smtplib.SMTP('smtp.gmail.com:587')   #If You want try to email from a gmail account. Comment above statement if you want to use this.

#To Establish TLS with the established cnnection with SMTP server.
server.starttls()  
#To verify the login authentication
server.login(username,password)  
#To send an email using the fields specified.
server.sendmail(From, Recipient, Messege)  
#To close the established SMTP Connection
server.close() 

print "Email has been sent"
