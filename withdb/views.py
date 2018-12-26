# to set register page as index
from django.shortcuts import redirect

def login_redirect(request):
	return redirect('/myapp/register')