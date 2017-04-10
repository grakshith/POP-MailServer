import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
def send(to_field,from_field,subject_field,body_field):
	msg = MIMEText(body_field)
	msg['To'] = email.utils.formataddr(('Recipient',
	                                    to_field))
	msg['From'] = email.utils.formataddr(('Author',
	                                      from_field))
	msg['Subject'] = subject_field

	server = smtplib.SMTP('127.0.0.1', 1025)
	server.set_debuglevel(True)  # show communication with the server
	try:
	    server.sendmail(from_field,
	                    [to_field],
	                    msg.as_string())
	finally:
	    server.quit()
