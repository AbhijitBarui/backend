from django.urls import path
from . import views

urlpatterns = [
    path('activate/<str:uid>/<str:token>', views.activate),
    path('password/reset/confirm/<str:uid>/<str:token>', views.password_reset_confirm),
]