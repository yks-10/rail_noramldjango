from django.db import models

# Create your models here.

class Train(models.Model):
    train_name=models.CharField(max_length=40)
    train_no=models.CharField(max_length=6)
    train_starting=models.CharField(max_length=20)
    train_ending=models.CharField(max_length=20)
    timing=models.DateTimeField()

    def __str__(self):
        return self.train_name

class Search(models.Model):
    train_starting = models.CharField(max_length=20)
    train_ending = models.CharField(max_length=20)
    timing = models.CharField(max_length=20)

    def __str__(self):
        return self.train_starting

class Booking(models.Model):
    name=models.CharField(max_length=20)
    addhaar_no=models.CharField(max_length=12,primary_key=True)
    count=models.IntegerField()

    def __str__(self):
        return self.addhaar_no