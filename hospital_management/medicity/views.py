from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def login(request):
	if request.method=='POST':
		# username = request.POST.get('form-username', None)
		# password = request.POST.get('form-password',None)


    template = loader.get_template("medicity/login.html")
    return HttpResponse(template.render())
# Create your views here.
