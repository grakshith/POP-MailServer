from django import forms

class ComposeForm(forms.Form):
	to=forms.EmailField(label='To',max_length=100)
	from_field=forms.EmailField(label='From',max_length=100)
	subject=forms.CharField(label='Subject',max_length=500)
	body=forms.CharField(label='Body')