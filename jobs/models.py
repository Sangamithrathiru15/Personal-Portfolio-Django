from django.db import models
from django.db.models.fields.files import ImageField

class Jobs(models.Model):
    image=models.ImageField(upload_to='image/')
    summary=models.CharField(max_length=200)
