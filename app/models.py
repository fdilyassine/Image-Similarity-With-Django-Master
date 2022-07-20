from django.db import models

# Create your models here.
class Vector(models.Model):
    #n_neighbor = models.IntegerField(null=True)
    vector = models.FileField(upload_to='app/img/')