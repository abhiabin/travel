from django.db import models


# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    dec=models.TextField()

class itemss(models.Model):
        name = models.CharField(max_length=250)
        img = models.ImageField(upload_to='pics')
        dec = models.TextField()





