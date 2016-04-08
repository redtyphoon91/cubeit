from django.conf.urls import url
from . import views

urlpatterns = [
    #10 listing all content of a user
    url(r'^(?P<userid>[0-9]+)/content/$', views.contents),

    #9 listing all cube of a user
    url(r'^(?P<userid>[0-9]+)/cube/$', views.cubes),

    #8 For sharing a content with other user
    url(r'^(?P<userid>[0-9]+)/content/(?P<contentid>[0-9]+)/share/(?P<newuserid>[0-9]+)/$', views.share_content),

    #7 sharing a cube with other user
    url(r'^(?P<userid>[0-9]+)/cube/(?P<cubeid>[0-9]+)/share/(?P<newuserid>[0-9]+)/$', views.share_cube),

    #6 For deleting a cube
	url(r'^(?P<userid>[0-9]+)/cube/(?P<cubeid>[0-9]+)/delete/$', views.delete_cube),


    #5 For deleting a content from a cube
	url(r'^(?P<userid>[0-9]+)/cube/(?P<cubeid>[0-9]+)/content/(?P<contentid>[0-9]+)/delete/$', views.contentcubedelete),

    #4 For adding a content to a cube
    url(r'^(?P<userid>[0-9]+)/cube/(?P<cubeid>[0-9]+)/content/(?P<contentid>[0-9]+)/$', views.contentcube),

    #3 For creating a content for a user, #10 For listing all contents of a user
    url(r'^(?P<userid>[0-9]+)/content/(?P<link>[\w+]+)/+$', views.content),

    #2 For creating a cube, #9 get all cube for a user
    url(r'^(?P<userid>[0-9]+)/cube/(?P<name>[\w+]+)/$', views.cube),
    #1 creating a user
    url(r'(?P<name>[\w+]+)/(?P<city>[\w.@+-]+)/$', views.user),
    
]