import smtplib
from email.message import EmailMessage


class MailClient :

    # Function to get credentials for connection

    def __init__(self,mail,password) :

        self.email = mail

        self.password = password

    #Function to send the mail

    def send(self,subject,body,alter,sender,to) : 


        msg = EmailMessage()

        # subject of the mail

        msg['Subject'] = subject 

        # sender 

        msg['From'] = sender

        # target

        msg['To'] = to

        # body

        msg.set_content(body)

        # HTML

        msg.add_alternative(alter,subtype='html')


        # sending the mail

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp :

            smtp.login(self.email,self.password)

            smtp.send_message(msg)
