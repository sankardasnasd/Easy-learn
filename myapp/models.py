from django.db import models

# Create your models here.

class Login(models.Model):
    Name = models.CharField(max_length=50)
    Password = models.CharField(max_length=10)
    Usertype = models.CharField(max_length=100)

class User(models.Model):
    Name = models.CharField(max_length=50)
    Phone = models.IntegerField(max_length=50)
    Email = models.CharField(max_length=50)
    Dob = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    Place = models.CharField(max_length=50)
    Post = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Pin = models.IntegerField(max_length=50)
    Photo = models.CharField(max_length=250)
    Password = models.CharField(max_length=50)
    C_password = models.CharField(max_length=50)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)

class Complaints(models.Model):
    compliant = models.CharField(max_length=200)
    date = models.DateField()
    status = models.CharField(max_length=300)
    replay = models.CharField(max_length=200)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class Reviews(models.Model):
    review = models.CharField(max_length=500)
    date = models.DateField()
    rating = models.CharField(max_length=20)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class uploads(models.Model):
    voicefilename = models.CharField(max_length=100)
    qafilename = models.CharField(max_length=100)
    date = models.DateField()
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)