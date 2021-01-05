from .views import one
from django.urls import path
from dialyworkstatus import views
from django.contrib.auth import views as v

urlpatterns=[
	path("",views.cehm,name='cehm'),
	path("register/",views.register,name='register'),
	path("changepwd/",views.changepwd,name='changepwd'),
	path("one/",views.one,name='one'),
	path("two/",views.two,name='two'),
	path("three/",views.three,name='three'),
	path("four/",views.four,name='four'),
	path("five/",views.five,name='five'),
	path("six/",views.six,name='six'),
	path("seven/",views.seven,name='seven'),
	path("eight/",views.eight,name='eight'),
	path("dashboard/",views.dashboard,name='dashboard'),
	path("login/",v.LoginView.as_view(template_name="sa/login.html"),name='login'),
	path("Profile/",views.Profile,name='Profile'),
	path("logout/",v.LogoutView.as_view(template_name="sa/login.html"),name='logout'),
	path("aboutUs/",views.aboutUs,name='aboutUs'),
	path("contact/",views.contact,name='contact'),
	path('upf/',views.updf,name="updf"),
	path('wrk/',views.wrklg,name="wk"),
	path('crwrk/',views.creationwrk,name='crw'),
	path('password_change/',v.PasswordChangeView.as_view(template_name="sa/changepwd.html"),name='password_change'),
	path('search/',views.search,name="search"),
	path('ceh/',views.ceh,name="ceh"),
	path('ceh0/',views.ceh0,name="ceh0"),
	path('ceh1/',views.ceh1,name="ceh1"),
	path('ceh2/',views.ceh2,name="ceh2"),
	path('ceh3/',views.ceh3,name="ceh3"),
	path('ceh4/',views.ceh4,name="ceh4"),
	path('ceh5/',views.ceh5,name="ceh5"),
	path('ceh6/',views.ceh6,name="ceh6"),
	path('ceh7/',views.ceh7,name="ceh7"),
	path('ceh8/',views.ceh8,name="ceh8"),
	path('cehm/',views.cehm,name="cehm"),
	path('onlineexam/',views.onlineexam,name="onlineexam"),
]


