"""
SMTP - Simple Mail Transfer Protocol
Dicates how email should be formatted, encrypted and relayed between mail servers.

IMAP - Internet Message Access Protocol
specifies how to communicate with an email provider’s server to retrieve emails sent to your email address.

TLS (port 587) and SSL (port 465) are both types of encryption, to connect to a mail server, we have to
do it using the right encrypting.
"""
# SMTP protocol client module
import smtplib

# Connecting to gmail mail server
smtp_server = 'mail.gmx.com'
smtp_obj = smtplib.SMTP(smtp_server, 587)
print(type(smtp_obj))

# If connection is unsuccessful, try port 465, with SSL
# smtp_obj = smtplib.SMTP_SSL(smtp_server, 465)

# Establishing the connection to the server
response = smtp_obj.ehlo()
print('Connecting...', response)  # Response code 250 means 'success'

# Enabling TLS encryption for connectiong
# Not necessary if SMPT_SSL was used
response = smtp_obj.starttls()
print('TLS...', response)  # Response code 220 means 'server ready'

# Credentials
login_email_addr = 'pythonpro@gmx.com'
login_password = 'pythonpro'

# Login to the server
smtp_obj.login(login_email_addr, login_password)
print('Log in...', response) # Response code 235 means 'authentication successful'

"""
Gmail has an additional security feature for Google accounts called
'application-specific passwords'.
"""

# Sending email
from_addr = login_email_addr
to_addr = 'ed.bldr@gmail.com'

# The start of the email body string must begin with 'Subject: \n' for the subject line of the email
body = 'Subject: !\nHello World from Python Pro!'

# @(sender_email, recipient_email, email_body)
response = smtp_obj.sendmail(from_addr, to_addr, body)
print('Sending email...', response)
"""
The return value from sendmail() is a dictionary. There will be one key-value pair
in the dictionary for each recipient for whom email delivery failed.
An empty dictionary means all recipients were successfully sent the email.
"""

# Disconnecting from the server
response = smtp_obj.quit()
print('Disconnecting...', response)  # Response code 221 means 'session close'
