from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=120)
	author = models.CharField(max_length=120)
	def __str__(self):
		return self.title

class UserRegistration(models.Model):
	fullname = models.CharField(max_length=120)
	email = models.EmailField(unique=True)
	username = models.CharField(unique=True, max_length=120)
	password = models.CharField(max_length=120)
	def __str__(self):
		return self.username

# class Trial(models.Model):
# 	name = models.CharField(max_length=120)
# 	email = models.CharField(max_length=120)
# 	def __str__(self):
# 		return self.name

