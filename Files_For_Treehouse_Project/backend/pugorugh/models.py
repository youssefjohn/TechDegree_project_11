from django.db import models

# Create your models here.



class Dog(models.Model):
    name = models.CharField(max_length=100, blank=True)
    image_filename = models.ImageField(default='static/images/dogs/')
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    size = models.CharField(max_length=1)














class UserDog(models.Model):
    user = models.CharField(max_length=100)
    dog = models.OneToOneField(Dog,on_delete=models.CASCADE)
    status = models.CharField(max_length=1)






class UserPref(models.Model):
    user = models.OneToOneField(UserDog, on_delete=models.CASCADE)
    age = models.CharField(max_length=1)
    gender = models.CharField(max_length=1)
    size = models.CharField(max_length=1)

