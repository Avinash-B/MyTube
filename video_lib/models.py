from django.db import models

# Create your models here.
class UploadModel(models.Model):
    file = models.FileField(upload_to='Videos/%Y/%m/%d/%H/%M/%S/')