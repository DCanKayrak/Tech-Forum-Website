import smtplib
from smtplib import SMTPException


def sendMail(to,msg):
    sender = 'danyal48@hotmail.com'
    password = '****'



    server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    server.starttls()
    server.login(sender,password)
    print('Login Success!')

    server.sendmail(sender,to,msg)