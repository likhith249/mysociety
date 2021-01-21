from django.shortcuts import render
from . models import Society,Member
from django.http import HttpResponse

# Create your views here.
def home(request):
    soc = Society.objects.all()
    print(soc)
    return HttpResponse('abc')