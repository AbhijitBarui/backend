from django.shortcuts import get_object_or_404
from rest_framework.serializers import Serializer, FileField
from rest_framework import serializers
from .models import Upload

class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']

class ViewFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ['id','content_type']

class ViewFileSerializer(serializers.ModelSerializer):
    file_id = serializers.SerializerMethodField()
    
    class Meta:
        model = Upload
        fields = ['id','content_type','file_id']

    def get_file_id(self, obj):
        file_id = self.context.get('file_id')
        return file_id