# Email Generator

from email.message import EmailMessage
# from app import password
import ssl
import smtplib

password = "pxtynhmqvccmmmpw"
email_sender = 'kaizhen970123@gmail.com'
email_password = password
email_receiver = 'kaizhen970123@gmail.com'

title = "Title"
body = "Email Body"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = title
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())