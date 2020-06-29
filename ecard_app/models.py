from django.db import models

# Create your models here.
class quotes(models.Model):
    quote = models.CharField(max_length=500)
    name = models.CharField(max_length=80)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class quotes2(models.Model):
    quote = models.CharField(max_length=500)
    name = models.CharField(max_length=80)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class quotes3(models.Model):
    quote = models.CharField(max_length=500)
    name = models.CharField(max_length=80)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
