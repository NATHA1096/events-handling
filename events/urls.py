from django.conf.urls import url
from . import views

app_name = 'events'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/', views.add_event, name='addEvent'),
    url(r'^logout', views.logout_request, name='logout'),
    url(r'^delete/(?P<idEvent>\d+)$', views.delete_event, name='deleteEvent'),
    url(r'^signUp/', views.signUp, name='signUp'),
    url(r'^edit/(?P<idEvent>\d+)$', views.edit_event, name='editEvent'),
]