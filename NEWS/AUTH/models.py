from django.contrib.auth.models import AbstractUser, User
from django.db import models

# class MyUser(AbstractUser):
#     photo = models.ImageField(upload_to='users/')
#     date_f_birth = models.DateTimeField()
#     address = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/', null=True, blank=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return f"{self.user.username}'s profile"