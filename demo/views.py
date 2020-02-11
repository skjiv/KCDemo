from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return HttpResponse('You\'re at the index.<a href="/secure">Secure</a>')

@login_required
def secure(request):
    return HttpResponse('Secure page. <a href="/openid/logout">Logout</a>')
