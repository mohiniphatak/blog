from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# from myapp.forms import RegistrationForm
from django.core.paginator import Paginator
from .forms import BlogForm
# from .forms import UserLoginForm
from .forms import UserRegistrationForm
from .forms import UserLoginForm
from .models import UserRegistration
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import viewsets
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth



class BlogView(viewsets.ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer

def addblog(request):
	if request.method == 'POST':
		form = BlogForm(request.POST)
	else:
		form = BlogForm()
	if form.is_valid():form.save(commit=True)	
	return render(request,'addblog.html',{'form':form})

def showblog(request):
	queryset = Blog.objects.all().order_by('title')
	# queryset = Blog.objects.filter(author="mohini").order_by('-title')
	p = Paginator(queryset,1)
	# number = request.GET.get('page')
	try:
		number = request.GET.get('page')
		pg = p.page(number)
	except:
		pg = p.page(1)
	return render(request,'showblog.html',{'blogs':pg})

# def register(request):
# 	if request.method =='POST':
# 		form = UserCreationForm(request.POST)
# 		if form.is_valid():form.save(commit=True)
# 		return redirect('/myapp/addblog')
# 	else:
# 		form = UserCreationForm()
# 		return render(request, 'registration.html', {'form':form})

# def register(request):
# 	if request.method =='POST':
# 		form = RegistrationForm(request.POST)
# 		if form.is_valid():form.save(commit=True)
# 		return redirect('/myapp/addblog')
# 	else:
# 		form = RegistrationForm()
# 		return render(request, 'registration.html', {'form':form})

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
	else:
		 form = UserRegistrationForm()
	if form.is_valid():form.save(commit=True)	
	return render(request,'registration.html',{'form':form})





# def login(request):
# 	login = UserLoginForm(request.POST or None)
# 	# username = request.GET['username']
# 	# password = request.GET['password']
# 	user = authenticate(request,username='phatakmohini@gmail.com',password='urmylife_11')
# 	if user:
# 		login(request,user)
# 		return render(request,'login.html',{'loginform':loginform})
# 	return render(request,'login.html',{})

def login(request):
	form = UserLoginForm(request.POST or None)
	if request.method == 'POST':
		username = request.POST.get['username']
		password = request.POST.get['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:

			login(request,user)
			return render(request,'login.html',{'form':form})
		else:
			return redirect('register.html')
			

	return render(request,'login.html',{'form':form})

def logout(request):
	logout(request)
	return render(request,'index.html',{})


def dashboard(request):
	return render(request,'dashboard.html',{})
