from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import UserRegistration
from .models import Blog

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('title','author')

# class RegistrationForm(UserCreationForm):
# 	email = forms.EmailField(required = True)

# 	class Meta:
# 		model = User
# 		fields = ('username','first_name','last_name','email','password1','password2')

# 	def save(self, commit=True):
# 		user = super(RegistrationForm, self).save(commit=False)
# 		user.firstname = self.cleaned_data['first_name']
# 		user.lastname = self.cleaned_data['last_name']
# 		user.email = self.cleaned_data['email']

# 		if commit:
# 			user.save()

# 		return user

class UserRegistrationForm(forms.ModelForm):
	class Meta:
		model = UserRegistration
		fields = ('fullname','email','username','password',)

class UserLoginForm(forms.ModelForm):
	class Meta:
		model = UserRegistration
		fields = ('username','password',)