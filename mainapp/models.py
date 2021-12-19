from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Address(models.Model):
      id = models.AutoField(primary_key=True)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      city = models.CharField(max_length=200)
      Address1 = models.CharField(max_length=200)
      Address2 = models.CharField(max_length=200)
      postalcode = models.CharField(max_length=200)
      phone = models.PositiveIntegerField()
      country = models.CharField(max_length=200)
      lastupdate = models.DateTimeField(blank=True)
      def __str__(self):
             return "%s" % (self.id)

class mediacatagory(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=200)
     def __str__(self):
             return "%s" % (self.name)

class media(models.Model):
    id = models.AutoField(primary_key=True)
    mediacatagory1 = models.ForeignKey(mediacatagory, on_delete=models.CASCADE , default=1)
    title = models.CharField(max_length=200)
    Discription = models.CharField(max_length=200)
    release_year = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()
    fulltext = models.CharField(max_length=200)
    lastupdate = models.DateTimeField(blank=True)
    media_status =models.BooleanField(default=False)
    def __str__(self):
             return "%s" % (self.id)
        
class loan(models.Model):
     id = models.AutoField(primary_key=True)
     userid = models.ForeignKey(User, on_delete=models.CASCADE)
     mediaid = models.ForeignKey(media, on_delete=models.CASCADE)
     loandate = models.DateTimeField(blank=True)
     returndate = models.DateTimeField(blank=True)
    
     def __str__(self):
             return "%s" % (self.id)
