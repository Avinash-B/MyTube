from django.db import models

# Create your models here.
music_path='Music/'
class UploadModel(models.Model):
    file = models.FileField(upload_to="Home/")