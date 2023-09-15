import smtplib

# Make SMTP Server
ob = smtplib.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()

# Login to your gmail
ob.login('ah32723272@gmail.com', 'kisnbiiaquoxngqa')

# Make Massage for sending
subject = 'Test Python'
body = 'I love Python'
message = 'Subject: {}\n\n{}'.format(subject, body)

# Make a list of sending gmails
list_add = ['alihaider7214408@gmail.com', 'networkking0097@gmail.com'] 

# Send the Mail
ob.sendmail('ah32723272@gmail.com', list_add, message)
print('Email sent successfully')

ob.quit()
