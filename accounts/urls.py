from django.urls import path
from . import views

urlpatterns = [
    path("userlist", views.userlist, name='userlist'),
    path("", views.index, name='index'),
    # path("sendmail", views.sendmail),
]