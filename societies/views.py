from django.shortcuts import render
from . models import Society,Member,Dues

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

# Create your views here.

@method_decorator(csrf_exempt)
def add_due(request):
	if request.method == 'POST':
		mem = Member.objects.get(name= request.POST.get('d1')) 
		soc = Society.objects.get(name= request.POST.get('d2'))
		try:
			dues = Dues.objects.get(member=mem,society=soc)
		except Dues.DoesNotExist:
			dues = None
		if dues is not None:
			d = request.POST.get('d3')
			dues.due = d
			dues.save()
			res = {
				'success': True,
				'message': 'member is not in society',
			}
		else:
			res = {
				'failure': False,
				'message': 'dues added',
			}
	return JsonResponse(res)

@method_decorator(csrf_exempt)
def create_society(request):
	if request.method == 'POST':
		name= request.POST.get('data1')
		address= request.POST.get('data2')
		if not Society.objects.filter(name=name).exists():
			Society.objects.create(name= name,address= address)
			res = {
				'success': True,
				'message': 'society created',
			}
		else:
			res = {
			'failure': False,
			'message': 'society name already taken',
			}
	return JsonResponse(res)

@method_decorator(csrf_exempt)
def create_member(request):
	if request.method == 'POST':
		mid= request.POST.get('d1')
		name= request.POST.get('d2')
		age= request.POST.get('d3')
		contact= request.POST.get('d4')
		address= request.POST.get('d5')

		if not Member.objects.filter(member_id=mid).exists():
			mem = Member(member_id= mid, name= name, age= age, 
				contact= contact, address= address)
			mem.save()
			res = {
				'success': True,
				'message': 'member created',
			}
		else:
			res = {
				'failure': False,
				'message': 'member already exists',
			}

	else:
		res = {
			'failure': False,
		}
	return JsonResponse(res)

@method_decorator(csrf_exempt)
def add_member(request):
	if request.method == 'POST':
		mem_name = request.POST.get('d1')
		data = request.POST.get('d2')
		dat=data.split(',')

		if not Member.objects.filter(name=mem_name).exists():
			res = {
				#'message': 'member does not exist'
				'failure': False,
			}
		else:
			mem = Member.objects.get(name=mem_name)
			if len(dat) + mem.society.count() > 3:
				res = {
					'message': 'member cannot be associated to more than 3 societies',
					'failure': False,
				}
			else:
				for d in dat:
					soc = Society.objects.get(name=d)
					if soc is not None:
						mem.society.add(soc)
					else:
						res = {
							'failure' : False,
			 			}
						break
				res = {
					'message': 'member added to societies',
					'success': True,
				}
	else:
		res = {
			'failure' : False,
		}
	
	return JsonResponse(res)