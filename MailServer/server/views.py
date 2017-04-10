from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import smtpd
import asyncore
from client.models import User,Message
import thread
class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to  :', rcpttos)
        print('Message length        :', len(data))
        print('Data                  :',data)
        subject=data.split('\n')[5].split()[1]
        body=data.split('\n')[7]
        user=User.objects.filter(email_id=str(rcpttos[0]))
        message=Message(to=str(rcpttos[0]),from_field=mailfrom,subject=subject,body=body,user=user[0])
        message.save()
        print user

def start(request):
	server = CustomSMTPServer(('127.0.0.1', 1025), None)
	#asyncore.loop()
	thread.start_new_thread(async,(None,))
	return HttpResponse("Server Started")

def async(self):
	asyncore.loop()
