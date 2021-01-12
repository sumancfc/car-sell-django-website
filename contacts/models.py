from django.db import models
from datetime import datetime


class Contact(models.Model):
       first_name = models.CharField(max_length=50)
       last_name = models.CharField(max_length=50)
       car_id = models.IntegerField()
       customer_need = models.CharField(max_length=100)
       car_title = models.CharField(max_length=100)
       city = models.CharField(max_length=100)
       state = models.CharField(max_length=100)
       email = models.EmailField(max_length=100)
       phone = models.CharField(max_length=100)
       message = models.TextField(blank=True)
       user_id = models.IntegerField(blank=True)   
       create_date = models.DateTimeField(default=datetime.now, blank=True)

       def __str__(self):
              return self.email