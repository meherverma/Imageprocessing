import smtplib
from email.message import EmailMessage

email=EmailMessage()
email['from']='meherverma'
email['to']='meherverma5@gmail.com'
email['subject']='Good Luck meher'

email.set_content('hi meher what are you doing')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('meherverma8@gmail.com', 'Niit@12345')
    smtp.send_message(email)
    print('email sent successfull')