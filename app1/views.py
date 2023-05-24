from django.shortcuts import render
from django.http import HttpResponse


def app1(request):
    return HttpResponse('Brother of Harshad Valli')

def app1html(request):
    return render(request,'app1html.html')



