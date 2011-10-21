from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns("",
				(r'^$','bookmarks.views.home'),
				(r'^new/$','bookmarks.views.new'),
				(r'^thanks/$','bookmarks.views.thanks'),
				(r'^delete/(?P<bookmark_id>\d+)$','bookmarks.views.delete'),
				(r'^edit/(?P<bookmark_id>\d+)$','bookmarks.views.edit'),
				)