from urllib import response
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import UserAccount
from rest_framework.response import Response
from .serializers import User, UserlistSerializer
from rest_framework.decorators import api_view

from django.core.mail import send_mail

def index(request, *args, **kwargs):
    return render(request, 'pages/index.html')

@api_view(['GET'])
def userlist(request):
    users = UserAccount.objects.all()
    serializer = UserlistSerializer(users, many=True)
    return Response(serializer.data)

# def sendmail(request):
#     send_mail(
#         'Hello please authenticate',
#         'Authenticate also known as Auth',
#         'aogit.simmifoundation@gmail.com',
#         ['abhijitongit@gmail.com','barui240@gmail.com'],
#         fail_silently=False
#     )
#     return redirect('userlist')