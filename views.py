# Create your views here.
from django.shortcuts import render_to_response

from django.http import HttpResponseRedirect
from django.template import RequestContext

#import from app's forms & models
from bookmarks.forms import new_bookmark
from bookmarks.models import bookmarks

def home(request):
	if request.user.is_authenticated():
		pool = bookmarks.objects.filter(user=request.user)
		return render_to_response('bookmarks_home.html',{ 'user' : request.user,'bookmarks': pool })
	else:
		return render_to_response('user_not_signed_in.html',{})

def new(request):
		if request.method == "POST":
			form = new_bookmark(request.POST)
			if form.is_valid():
				user = request.user
				name = form.cleaned_data['name']
				url = form.cleaned_data['url']
				newbookmark = bookmarks.objects.create(
														user = user,
														name = name,
														url = url
														)
				newbookmark.save()
				return HttpResponseRedirect('/bookmarks/thanks')
		else:
			form = new_bookmark()
		return render_to_response('new_bookmark.html',{'form':form},context_instance=RequestContext(request))

def thanks(request):
	return render_to_response('bookmarks_thanks.html',{})
