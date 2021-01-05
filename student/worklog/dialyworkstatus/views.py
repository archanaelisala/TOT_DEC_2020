from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from dialyworkstatus.forms import UsReg,Updf,Imp,wrkform,ChgPwd
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from worklog import settings
from django.contrib import messages
from dialyworkstatus.models import Worklog,ChangePwd,ModelName
from django.db.models import Q
from embed_video.backends import detect_backend




#from dialyworkstatus.models import ImPfle
# Create your views here.
# my_video = detect_backend('http://www.youtube.com/watch?v=H4tAOexHdR4')


@login_required
def onlineexam(request):
	results=Exam.objects.all()
	return render(request,'sa/Exam.html',{"Exam":results})


def cehm(request):
	return render(request,'sa/chem.html')
@login_required
def ceh(request):
	return render(request,'sa/ceh.html')
def ceh0(request):
	return render(request,'sa/ceh1.html')	
@login_required
def ceh1(request):
	return render(request,'sa/ceh1-1.html')
@login_required
def ceh2(request):
	return render(request,'sa/ceh1-2.html')
@login_required
def ceh3(request):
	return render(request,'sa/ceh1-3.html')
@login_required
def ceh4(request):
	return render(request,'sa/ceh1-4.html')
@login_required
def ceh5(request):
	return render(request,'sa/ceh1-5.html')
@login_required
def ceh6(request):
	return render(request,'sa/ceh1-6.html')
@login_required
def ceh7(request):
	return render(request,'sa/ceh1-7.html')
@login_required
def ceh8(request):
	return render(request,'sa/ceh1-8.html')


def searchMatch(query, item):
    if query in item.product_name or query in item.category:
        return True
    else:
        return False


def search(request):
    query= request.GET.get('search')
    one=['Certified Ethical Hacking Certification','ceh']
    two=['GIAC Penetration Tester','giac','GIAC']
    three=['Offensive Security Certified Professional','oscp','OSCP']
    four=['CREST','crest']
    five=['Foundstone Ultimate Hacking','Foundstone','foundstone']
    six=['Certified Penetration Testing Consultant','cptc','CPTC']
    seven=['Certified Penetration Testing Engineer','cpte','CPTE']
    eight=['Ethical hacking course for Beginers','Ethical hacking','ethical hacking']
    if query in one:
    	    return redirect( 'one')
    elif query in two:
    	    return redirect( 'two')
    elif query in three:
    	    return redirect('three')
    elif query in four:
    	    return redirect( 'four')
    elif query in five:
    	    return redirect( 'five')
    elif query in six:
    	    return redirect('six')
    elif query in seven:
    	    return redirect('seven')
    elif query in eight:
    	    return redirect('eight')
    elif query==0:
    	return messages.success(request,"No results found..")
    return render(request,'sa/search.html')



def wrklg(request):
	p = Worklog.objects.filter(m_id=request.user.id)
	return render(request,'sa/worklog.html',{'y':p})

def creationwrk():
	if request.method == "POST":
		r = wrkform(request.POST)
		if r.is_valid():
			t = r.save(commit=False)
			t.m_id = request.user.id
			t.save()
			messages.success(request,"Your task updated successfully")
			return redirect('/wrk')
	messages.info(request,"sorry you have already submitted today")
	r = wrkform()
	return render(request,'ds/crwrk.html',{'d':r})



def home(request):
	return render(request,'sa/home.html')
def register(request):
	if request.method=='POST':
		t=UsReg(request.POST)
		if t.is_valid():
			user=t.save()
			adml = user.email
 			#pas = user.password
			msg = "Hi {}  register successfully your email is {} and password is {}".format(user.username,user.email,user.password)
			sub = "Test mail"
			sd = settings.EMAIL_HOST_USER
			to = send_mail(sub,msg,sd,[adml])
			if to == 1:
				messages.success(request,"mail sent successfully")
				return render(request,'sa/login.html')
	t=UsReg()
	return render(request,'sa/register.html',{'y':t})


@login_required
def changepwd(request):
	if request.method=='POST':
		# a=User.objects.get(username='{}'.format(user.username))
		a=ChgPwd(request.POST)
		if a.is_valid():
			a.save()
			messages.success(request," successfully Changed password")
			return redirect('/dashboard')
	a=ChgPwd()
	return render(request,'sa/changepwd.html',{'y':a})

# @login_required
def one(request):
	videos=ModelName.objects.all()
	return render(request,'sa/1.html',{'videos':videos})
def two(request):
	return render(request,'sa/2.html')
def three(request):
	return render(request,'sa/3.html')
def four(request):
	return render(request,'sa/5.html')
def five(request):
	return render(request,'sa/4.html')
def six(request):
	return render(request,'sa/3.html')
def seven(request):
	return render(request,'sa/2.html')
def eight(request):
	return render(request,'sa/1.html')

@login_required
def dashboard(request):
	return render(request,'sa/dashboard.html')

@login_required
def Profile(request):
	return render(request,'sa/Profile.html')



@login_required
def updf(request):
	if request.method == "POST":
		p = Updf(request.POST,instance=request.user)
		k = Imp(request.POST,request.FILES,instance=request.user.impfle)
		if p.is_valid() and k.is_valid():
			p.save()
			k.save()
			messages.info(request,'{} profile updated successfully'.format(request.user.username))
			return redirect('/Profile')
	p = Updf(instance=request.user)
	y =Imp(instance=request.user.impfle)
	return render(request,'sa/upfle.html',{'h':p,'u':y})



@login_required
def mailsnd(request):
	pq = User.objects.values_list("email",flat=True)
	# print(pq)
	if request.method == "POST":
		# rec = request.POST['sndml'].split(",")
		# print(rec)
		rec = []
		adml = request.user.email
		rs = list(filter(None,pq))
		for m in rs:
			if m=="" or m==adml:
				continue
			else:
				rec.append(m)
		print(rec)
		sub = request.POST['subject']
		msg = request.POST['messg']
		sd = settings.EMAIL_HOST_USER
		t = send_mail(sub,msg,sd,rec)
		if t == 1:
			return redirect("/ml")
		return HttpResponse("Didnt send mail to particular person")
	return render(request,'sa/mailsending.html')

# def register(request):
# 	if request.method == "POST":
# 		t = UsReg(request.POST)
# 		if t.is_valid():
# 			user=t.save()
# 			messages.success(request,"User registered Successfully")
# 			#return redirect('/login')
# 			adml = user.email
# 			pas = user.password
# 			msg = "Hi {}  register successfully your email is {} and password is {}".format(user.username,user.email,user.password)
# 			sub = "Test mail"
# 			sd = settings.EMAIL_HOST_USER
# 			to = send_mail(sub,msg,sd,[adml])
# 			if to == 1:
# 				return messages.primary("A mail sent to your account")
# 				return redirect('/login')
# 				return messages.primary("A mail sent to your account")
# 		messages.warning(request,'mail not sent')
# 	messages.error(request,'Registration Failed')
# 	t = UsReg()
# 	return render(request,'sa/register.html',{'y':t})


def aboutUs(request):
	return render(request,'sa/about.html')
def contact(request):
	return render(request,'sa/contact.html')







# def search(request):
#     search_term = ''

#     if 'search' in request.GET:
#         search_term = request.GET['search']
#         articles = User.objects.all().filter(feeder__icontains=search_term) 

#     articles = User.objects.all()

#     return render(request, 'sa/search.html', {'articles' : articles, 'search_term': search_term })    