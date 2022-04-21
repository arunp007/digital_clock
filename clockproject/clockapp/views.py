from django.shortcuts import render
from django.http import HttpResponse

def clock(request):
    return render(request,'clock.html')

