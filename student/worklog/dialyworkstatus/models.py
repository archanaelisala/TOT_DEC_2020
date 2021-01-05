from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from embed_video.fields import EmbedVideoField
from django.urls import reverse


#Create your models here.


class Exam(models.Model):
	Question=models.CharField(max_length=256)
	Option1=models.CharField(max_length=256)
	Option2=models.CharField(max_length=256)
	Option3=models.CharField(max_length=256)
	Option4=models.CharField(max_length=256)
	Corrans=models.CharField(max_length=256)
	class Meta:
		db_table='onlineexam'



class PageTitleMixin(object):
  def get_page_title(self, context):
    return getattr(self, "page_title", context["user_settings"].site_title)



class ModelName(models.Model):
    video = models.FileField(upload_to="video/%y")


class ChangePwd(models.Model):
	password1=models.CharField(max_length=256)
	password2=models.CharField(max_length=256)
	

class ImPfle(models.Model):
	u = models.OneToOneField(User,on_delete=models.CASCADE)
	im = models.ImageField(upload_to="Profile/",null=True,default="images2.jpg")
	age = models.IntegerField(default=18) 

@receiver(post_save,sender=User)
def Crtpfle(sender,instance,created,**kwargs):
	if created:
		ImPfle.objects.create(u=instance)



class Worklog(models.Model):
	wks = [('yes','completed'),('No','Not completed')]
	date = models.DateField()
	description = models.TextField()
	workstatus = models.CharField(choices=wks,max_length=10)
	m = models.ForeignKey(User,on_delete=models.CASCADE)