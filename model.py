from django.db import models
from django.utils import timezone

class Contact(models.Model):
  name = models.CharField(max_length=200)
  second_name = models.CharField(max_length=200) 
  email = models.EmailField(unique=true)
  phone = models.CharField(max_length=15)
  note = models.TextField(max_length=300)
  add_date = models.DateTimeField(
        default = timezone.now)
           
           
 def __str__(self):
    return self.title

