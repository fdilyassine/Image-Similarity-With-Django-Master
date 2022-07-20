from django.db import models

# Create your models here.
class Image(models.Model):
    #n_neighbor = models.IntegerField(null=True)
    image = models.ImageField(upload_to='app/img/')