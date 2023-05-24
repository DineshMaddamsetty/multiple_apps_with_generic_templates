from django.shortcuts import render
from django.http import HttpResponse


def app2(request):
    return HttpResponse('Dinesh Maddamsetty')

def app2html(request):
    return render(request,'app2html.html')

# Create your views here.
