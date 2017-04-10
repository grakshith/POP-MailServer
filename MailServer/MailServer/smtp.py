import smtpd
import asyncore
from client.models import User,Message

class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to  :', rcpttos)
        print('Message length        :', len(data))
        print('Data                  :',data)
        subject=data.split('\n')[5].split()[1]
        #user=User.objects.filter(email_id=rcpttos)
        #message=Message(to=rcpttos,from_field=mailfrom,subject=subject)

def start():
	server = CustomSMTPServer(('127.0.0.1', 1025), None)
	asyncore.loop()