from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=50)
	email_id=models.EmailField(max_length=100)
	def __str__(self):
		return self.name

class Message(models.Model):
	to=models.EmailField(max_length=100)
	from_field=models.EmailField(max_length=100)
	subject=models.CharField(max_length=500)
	body=models.TextField()
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.subject+' -- '+self.to)
	
