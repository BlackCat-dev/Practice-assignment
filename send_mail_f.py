import smtplib
import email.message



def send_mail(username,password,recv, subject, message):
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(username,password)
        msg = 'Subject : '+ subject + '\n\n' + message
        s.sendmail(username, recv, msg)
      
