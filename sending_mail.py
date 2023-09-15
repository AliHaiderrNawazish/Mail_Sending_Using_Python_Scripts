import smtplib

# Make SMTP Server
ob = smtplib.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()

# Login to your gmail
ob.login('your email', 'app password')

# Make Massage for sending
subject = 'your subject'
body = 'your massage'
message = 'Subject: {}\n\n{}'.format(subject, body)

# Make a list of sending gmails
list_add = ['client1@gmail.com', 'client2@gmail.com'] 

# Send the Mail
ob.sendmail('you email', list_add, message)
print('Email sent successfully')

# close this program
ob.quit()
