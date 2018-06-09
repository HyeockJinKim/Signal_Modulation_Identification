from django.db import models

# Create your models here.
class UploadModel(models.Model):
    file = models.FileField(null=True)