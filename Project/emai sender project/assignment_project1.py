import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "sg0175043@gmail.com"
sender_password = "wkbkkipaimdhsjal"

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, sender_password)
reciver_email = input("enter sender message to send email:")
Subject = input("enter subject :")
message = input("enter your message :")
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = reciver_email
msg['Subject'] = Subject
body = message
msg.attach(MIMEText(body, 'plain'))

# Send the email
server.sendmail(sender_email,reciver_email, msg.as_string())
server.quit()
