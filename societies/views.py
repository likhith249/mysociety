from django.shortcuts import render
from . models import Society,Member,Dues

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

# Create your views here.

@method_decorator(csrf_exempt)
def add_due(request):
	if request.method == 'POST':
		mem = Member.objects.get(name= request.POST.get('d1')) 
		soc = Society.objects.get(name= request.POST.get('d2')) 
		Dues.objects.create(member= mem, society=soc, due=request.POST.get('d3'))
		res = {
			'success': True,
			}
	return JsonResponse(res)


@method_decorator(csrf_exempt)
def create_society(request):
	if request.method == 'POST':
		name= request.POST.get('data1')
		address= request.POST.get('data2')
		Society.objects.create(name= name,address= address)
		res = {
			'success': True,
			}
	return JsonResponse(res)

@method_decorator(csrf_exempt)
def add_member(request):
	if request.method == 'POST':
		mid= request.POST.get('d1')
		name= request.POST.get('d2')
		age= request.POST.get('d3')
		contact= request.POST.get('d4')
		address= request.POST.get('d5')
		mem = Member(member_id= mid, name= name, age= age, 
			contact= contact, address= address)
		mem.save()
		data= request.POST.get('d6')
		soc = Society.objects.get(name= data)
		mem.society.add(soc)	
		res = {
			'success': True,
			}
	return JsonResponse(res)	




    