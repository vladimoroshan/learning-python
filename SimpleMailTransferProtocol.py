#! python3
# send_email.py - Skeleton to automating sending emails. We can add loops, spreadsheets etc

import smtplib

email = 'your_email_address@gmail.comm' # change to your Gmail address 
password = input('Please enter your password: ')

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587) # for other servers port may change
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(your_email, your_password)

to = input('Please enter recipient email address: ')
subject = input('What is the subject? ')
text = input('Write your message: ')

sendmail_status = smtp_obj.sendmail(email, to, 'Subject: {}\n{}'.format(subject, text))
if sendmail_status != {}:
	print('There was a problem sending email to {}: {}'.format(email, sendmail_status))
smtp_obj.quit()

