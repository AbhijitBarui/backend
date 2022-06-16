from django.db import models

class Upload(models.Model):
    file_uploaded = models.FileField(upload_to='files/%Y/%m/%d/')
    content_type = models.CharField(max_length=500, blank=True, null=True)