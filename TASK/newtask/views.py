from django.shortcuts import render
from django.http import HttpResponse
from newtask.models import College

# Create your views here.

def student(request):
	if request.method == 'POST':
		studentname = request.POST.get('sname')
		rollno = request.POST.get('rollno')
		semail = request.POST.get('semail')
		spassword = request.POST.get('spassword')
		scollegename = request.POST.get('scollegename')
		sbranch = request.POST.get('sbranch')
		smobile = request.POST.get('smobile')
		College.objects.create(studentname=studentname,rollno=rollno,semail=semail,spassword=spassword,scollegename=scollegename,sbranch=sbranch,smobile=smobile)
		return HttpResponse("<h1>RECORD INSERTED</h1>")
	return render(request,'newtask/student.html')



def faculty(request):
	if request.method == 'POST':
		facultyname = request.POST.get('fname')
		facultyid = request.POST.get('fid')
		femail = request.POST.get('femail')
		fpassword = request.POST.get('fpassword')
		fcollegename = request.POST.get('fcollegename')
		fbranch = request.POST.get('fbranch')
		fmobile = request.POST.get('fmobile')
		#facultySal = request.POST.get('fsal')
		College.objects.create(facultyname=facultyname,facultyid=facultyid,femail=femail,fpassword=fpassword,fcollegename=fcollegename,fbranch=fbranch,fmobile=fmobile)
		return HttpResponse("<h1> FACULTY RECORD INSERTED</h1>")
	return render(request,'newtask/faculty.html')



def login(request):
 	if request.method == 'POST':
 		username = request.POST.get('uname')
 		pwd = request.POST.get('pswd')
 		
 		student = College.objects.all().filter(semail=username,spassword=pwd)
 		faculty = College.objects.all().filter(femail=username,fpassword=pwd)

 		if student:
 			return render(request,'newtask/studentpage.html')
 		elif faculty:
 			return HttpResponse("<h1>Welcome Faculty</h1>")
 		else:
 			return HttpResponse("<h1>INVALID USERNAME AND PASSWORD</h1>")


 	return render(request,'newtask/login.html')











