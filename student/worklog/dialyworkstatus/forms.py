from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from dialyworkstatus.models import ImPfle
from dialyworkstatus.models import Worklog,ChangePwd



class ChgPwd(ModelForm):
	class Meta:
			
		model=ChangePwd
		fields =["password1","password2"]
		widgets ={
		"password1":forms.PasswordInput(attrs={
			"class":"form-control",
			"placeholder":"Enter password",
			}),
		"password2":forms.PasswordInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Confirm password",
			})
		}

	
class UsReg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Create Your Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Confirm Password"}))
	
	class Meta:
			
		model = User
		fields =["username","email","first_name","last_name"]
		widgets ={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Emailid",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Last Name",
			}),
		}

class Updf(ModelForm):
	class Meta:
		model = User
		fields =["username","email","first_name","last_name"]
		widgets ={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update Email id",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Last Name",
			}),

		}

class Imp(ModelForm):
	class Meta:
		model = ImPfle
		fields = ["age","im"]
		widgets = {
		"age":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Update Your Age",
			})
		}







class wrkform(forms.ModelForm):
	class Meta:
		model = Worklog
		fields = ["date","description","workstatus"]
		widgets={
		"date":forms.DateInput(attrs={
			"class":"form-control",
			"type":"date",
			}),
		"description":forms.Textarea(attrs={
			"class":"form-control",
			"rows":5,
			"cols":10,
			"placeholder":"Enter your Task",
			}),
		"workstatus":forms.Select(attrs={
			"class":"form-control",
			}),
		}




