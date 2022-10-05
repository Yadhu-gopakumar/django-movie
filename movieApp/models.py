from email.policy import default
from django.db import models

# Create your models here.
class movie(models.Model):
    img=models.ImageField(upload_to='images',default='images/default.png')
    year=models.IntegerField(default='2022')
    name=models.CharField(max_length=100,default='movie title')
    desc=models.TextField(default='movie description!!')

    def __str__(self):
        return self.name   