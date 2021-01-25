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
		try:
			mem = Member.objects.get(name= request.POST.get('member'))
		except Member.DoesNotExist:
			mem = None
		try:
			soc = Society.objects.get(name= request.POST.get('society'))
		except Society.DoesNotExist:
			soc = None
		
		if mem and soc is not None:

			try:
				dues = Dues.objects.get(member=mem,society=soc)
			except Dues.DoesNotExist:
				dues = None
			if dues is not None:
				d = request.POST.get('dues')
				dues.due = d
				dues.save()
				res = {
					'success': True,
					'message': 'dues added',
				}
			else:
				res = {
					'Success': False,
					'message': 'member and society not associated',
				}
		else:
			res = {
				'Success': False,
				'message': 'member or society does not exist'
			}
	else:
		res = {
			'Success': False,
			'message': 'method is not post',
		}
	return JsonResponse(res)

@method_decorator(csrf_exempt)
def create_society(request):
	if request.method == 'POST':
		name= request.POST.get('name')
		address= request.POST.get('address')
		if not Society.objects.filter(name=name).exists():
			Society.objects.create(name= name,address= address)
			res = {
				'success': True,
				'message': 'society created',
			}
		else:
			res = {
			'Success': False,
			'message': 'society name already taken',
			}
	return JsonResponse(res)

@method_decorator(csrf_exempt)
def create_member(request):
	if request.method == 'POST':
		mid= request.POST.get('id')
		name= request.POST.get('name')
		age= request.POST.get('age')
		contact= request.POST.get('contact')
		address= request.POST.get('address')

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
				'Success': False,
				'message': 'member name already taken',
			}

	else:
		res = {
			'Success': False,
			'message': 'method is not post',
		}
	return JsonResponse(res)

@method_decorator(csrf_exempt)
def add_member(request):
	if request.method == 'POST':
		mem_name = request.POST.get('name')
		data = request.POST.get('societies')
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
							'success' : False,
			 			}
						break
				res = {
					'message': 'member added to societies',
					'success': True,
				}
	else:
		res = {
			'success': False,
			'message': 'method is not post'
		}
	
	return JsonResponse(res)