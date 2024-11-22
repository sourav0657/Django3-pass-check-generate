from xml.dom.pulldom import CHARACTERS
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    CHARACTERS = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        CHARACTERS.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('SpecialCase'):
        CHARACTERS.extend(list('!@#$^&*()'))
    if request.GET.get('Numbers'):
        CHARACTERS.extend(list('1234567890'))

    length = int(request.GET.get('length',6))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(CHARACTERS)

    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')
