import os
import mimetypes
from django.utils.encoding import smart_str
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Upload
from rest_framework.response import Response
from .serializers import UploadSerializer, ViewFilesSerializer, ViewFileSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.viewsets import ViewSet
from django.core.mail import send_mail
from django.views.static import serve 

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer
    def list(self, request):        #it works as a get request
        files = Upload.objects.all()
        serializer = ViewFilesSerializer(files, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None): #single fetcher
        file = get_object_or_404(Upload, id=pk)
        file_id = file.id
        serializer = ViewFileSerializer(file, many=False, context={'file_id': file_id})
        return Response(serializer.data)

    def create(self, request):      #it works as a post request
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        upload = Upload(file_uploaded=file_uploaded, content_type=content_type)
        upload.save()
        response = "1"
        return Response(response)

@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def download_file(request, id):
    file = get_object_or_404(Upload, id=id)
    filepath = file.file_uploaded.url
    filename = filepath.split("/")[-1]
    path = open(filepath, 'r')

    # mime_type, _ = mimetypes.guess_type(filepath)
    # # Set the return value of the HttpResponse
    # ##response = HttpResponse(path, content_type=mime_type)
    # response = HttpResponse(mimetype='application/force-download')
    # # Set the HTTP header for sending to browser
    # response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
    # response['X-Sendfile'] = smart_str(filepath)
    # # Return the response value
    # return response
    # return (request, os.path.basename(filepath),os.path.dirname(filepath))
    #return HttpResponse(f'<a href="//{filepath}" download="{filepath}">download</a>')

    response = HttpResponse(content_type='application/force-download') # mimetype is replaced by content_type for django 1.7
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
    response['X-Sendfile'] = smart_str(filepath)
    # It's usually a good idea to set the 'Content-Length' header too.
    # You can also set any other required headers: Cache-Control, etc.
    return response


# @api_view(['GET'])
# def viewfiles(request):
#     files = Upload.objects.all()
#     serializer = ViewFilesSerializer(files, many=True)
#     return Response(serializer.data)