from django.db import models

# Create your models here.
class UploadModel(models.Model):
    file = models.FileField(upload_to="Home/")
    name = models.CharField(max_length=200, default="")