from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    state_of_residence = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sold_status = models.BooleanField(default=False) 
    mark_delete = models.BooleanField(default=False)
    buyers = models.ManyToManyField(Buyer, through="BuyerInterest")

    def __str__(self):
        return self.name

class BuyerInterest(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    is_new_owner = models.BooleanField(default=False)
