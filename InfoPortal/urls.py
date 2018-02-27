from django.conf.urls import url 
from InfoPortal import views 

urlpatterns = [
  # The home view ('/InfoPortal/') 
  url(r'^$', views.home, name='home'), 
  # Explicit home ('/InfoPortal/home/') 
  url(r'^home/$', views.home, name='home'), 
  # Redirect to get token ('/InfoPortal/landing/')
  url(r'^landing/$', views.landing, name='landing'),
 
  # Main view ('/InfoPortal/main/')
  #url(r'^main/$', views.BlogIndex.as_view(), name='main2'),
   url(r'^main/$', views.main, name='main'),
  #Logout
   url(r'^logout', views.logout, name='logout'),
   
]

