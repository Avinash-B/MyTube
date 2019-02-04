from django.db import models

# Create your models here.
img_path='Images/'
class UploadModel(models.Model):
    file = models.FileField(upload_to="Images/")