from django.db import models

from datetime import datetime



class Realtor(models.Model):
    Name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to= 'photo/%Y/%m/%d/')
    description =models.TextField(blank=True)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length = 30)
    is_mvp = models.BooleanField(default=False)
    hire_date= models.DateTimeField(default= datetime.now,blank=True)
    def __str__(self):
        return self.Name
