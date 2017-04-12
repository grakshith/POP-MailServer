from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$',views.home,name='redirect'),
	url(r'^login/$',auth_views.login,{'template_name':'client/login.html'}, name='login'),
	url(r'^compose/$',views.compose,name='compose'),
	url(r'^sent/$',views.sent,name='sent'),
	url(r'^logout/$',views.user_logout,name='logout'),
	url(r'^view/(?P<urlhash>.*)/',views.view_mail,name='view_mail'),
]
