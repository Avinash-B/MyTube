from django.db import models

# Create your models here.
video_path='Videos/'
class UploadModel(models.Model):
    file = models.FileField(upload_to=video_path)