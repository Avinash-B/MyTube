from django.db import models

# Create your models here.
doc_path='Docs/'
class UploadModel(models.Model):
    file = models.FileField(upload_to=doc_path)