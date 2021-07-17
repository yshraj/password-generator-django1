from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')


def password(request):

    thepassword=''

    char= list('abcdefghijklmnopqrstuvwxyz')
    if (request.GET.get('Uppercase')):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUV'))
    if (request.GET.get('Specialcharacters')):
        char.extend(list('!@#$%^&*'))
    if (request.GET.get('Numbers')):
        char.extend(list('1234567890'))

    length= int(request.GET.get('LENGTH'))

    for x in range(length):
        thepassword+=random.choice(char)

    return render(request,'generator/password.html',{'password':thepassword})
