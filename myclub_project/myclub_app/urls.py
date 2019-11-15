from django.conf.urls import url

# This syntax imports all of the functions and classes
# inside the views.py in the same folder.
from . import views

urlpatterns = [
    url(r'^home/$', views.home_page),
    url(r'^myclub_app/$', views.main_page),
    url(r'^profile/$', views.userHistogram.as_view())

]
