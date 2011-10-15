from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns("",
				(r'^$','bookmarks.views.home'),
				(r'^new/$','bookmarks.views.new'),
				(r'^thanks/$','bookmarks.views.thanks'),
				)