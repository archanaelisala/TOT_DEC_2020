from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Update(models.Model):
    genders = [('Female', 'Female'),
               ('Male', 'Male')]
    age = models.IntegerField(default=20)
    gender = models.CharField(max_length=7, choices=genders)
    image = models.ImageField(upload_to='profile_pics/', default='profile.png')
    p = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def CreateProfile(sender, instance, created, **kwargs):
    if created:
        Update.objects.create(p=instance)
