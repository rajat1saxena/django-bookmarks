from django.forms import ModelForm
from bookmarks.models import bookmarks

class new_bookmark(ModelForm):
	class Meta:
		model = bookmarks
		exclude = ('user',)
	 