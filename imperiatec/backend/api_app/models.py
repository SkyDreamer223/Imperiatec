from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    

    def __str__(self):
        return self.username
    
class Arrivals(models.Model):
    arrival_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,related_name="arrivals", on_delete=models.CASCADE)
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    
    def __str__(self):
        return self.arrival_date



