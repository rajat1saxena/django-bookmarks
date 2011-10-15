from django import forms

class new_bookmark(forms.Form):
	name = forms.CharField(max_length = 100)
	url = forms.URLField()