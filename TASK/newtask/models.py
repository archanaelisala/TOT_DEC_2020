from django.db import models

# Create your models here.
#class StudentFaculty(models.Model):
	#for student
	# studentname = models.CharField(max_length=30)
	# facultyname = models.CharField(max_length=30)
	# rollno = models.CharField(max_length=20)
	# facultyid = models.CharField(max_length=20)
	# email = models.EmailField(max_length=30)
	# password = models.CharField(max_length=20)
	# collegename = models.CharField(max_length=50)
	# branch = models.CharField(max_length=10)
	# mobile = models.IntegerField()


class College(models.Model):
	#for student
	studentname = models.CharField(max_length=30)
	facultyname = models.CharField(max_length=30)

	rollno = models.CharField(max_length=20)
	facultyid = models.CharField(max_length=20)

	semail = models.EmailField(max_length=30)
	femail = models.EmailField(max_length=30)

	spassword = models.CharField(max_length=20)
	fpassword = models.CharField(max_length=20)

	scollegename = models.CharField(max_length=50)
	fcollegename = models.CharField(max_length=50)

	sbranch = models.CharField(max_length=10)
	fbranch = models.CharField(max_length=10)

	smobile = models.IntegerField(null=True)
	fmobile = models.IntegerField(null=True)

	#facultySal = models.IntegerField()