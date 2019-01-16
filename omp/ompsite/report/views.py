from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.core.exceptions import ValidationError
from .models import Evaluator, Property, Report, User
from .forms import EvaluatorForm, PropertyForm, ReportRequestForm, ReportCompleteForm, UserForm



def index(request):
	context = {}
	return render(request, 'report/index.html', context)

def list_evaluator(request):
	evaluator_list = Evaluator.objects.all()
	template = loader.get_template('report/evaluator_list.html')
	context = {
		  'evaluator_list': evaluator_list,
	}
	return HttpResponse(template.render(context,request))

def create_evaluator(request):
	if request.method == 'POST':
		form = EvaluatorForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			form.save()
			return HttpResponseRedirect('/report/evaluator/list/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = EvaluatorForm()
		context = {
			'form' : form
		}

	return render(request, 'report/evaluator_create.html', context)
	
def evaluator_detail(request, evaluator_id):
    try:
        evaluator = Evaluator.objects.get(pk=evaluator_id)
    except Evaluator.DoesNotExist:
        raise Http404("Evaluator does not exist")
    return render(request, 'report/evaluator_detail.html', {'evaluator': evaluator})

def user_list(request):
	user_list = User.objects.all()
	template = loader.get_template('report/user_list.html')
	context = {
		  'user_list': user_list,
	}
	return HttpResponse(template.render(context,request))

def user_create(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			form.save()
			return HttpResponseRedirect('/report/user/list/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = UserForm()
		context = {
			'form' : form
		}

	return render(request, 'report/user_create.html', context)
	
def user_detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'report/user_detail.html', {'user': user})


def report_list(request):
	report_list = Report.objects.all()
	template = loader.get_template('report/report_list.html')
	context = {
		  'report_list': report_list,
	}
	return HttpResponse(template.render(context,request))

def report_create(request):
	if request.method == 'POST':
		form = ReportRequestForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			form.save()
			return HttpResponseRedirect('/report/report/list/')
		else:
			raise ValidationError("Form has an invalid input")

	# if a GET (or any other method) we'll create a blank form
	else:
		form = ReportRequestForm()
		context = {
			'form' : form
		}

	return render(request, 'report/report_create.html', context)
	
#def report_detail(request, report_id):
  #  try:
    #    report = Report.objects.get(pk=report_id)
#    except Report.DoesNotExist:
  #      raise Http404("Report does not exist")
  #  return render(request, 'report/report_detail.html', {'report': report})

def report_update(request, report_id):
	try:
		report = Report.objects.get(pk=report_id)
	except Report.DoesNotExist:
		raise Http404("Report does not exist")
	if request.method == 'POST':
		form = ReportCompleteForm(request.POST, request.FILES, instance=report)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			form.save()
			return HttpResponseRedirect('/report/report/list/')
		else:
			raise ValidationError("Form has an invalid input")

	# if a GET (or any other method) we'll create a blank form
	else:
		form = ReportCompleteForm(instance=report)
		context = {
			'report' : report,
			'form' : form
		}
		return render(request, 'report/report_update.html', context)
	
def get_or_create_property(request):
	form = PropertyForm(request.POST)
	pincode = form.cleaned_data['pincode']
	locality = form.cleaned_data['locality']
	name = form.cleaned_data['name']
    try:
    	#TODO: check if db index is created on search fields
        properties = Property.objects.filter(pincode__exact=pincode,
        	locality__contains=locality, name__contains=name)
        # handle multiple property matches
        property_id = properties[0].id
    except Property.DoesNotExist:
    	if form.is_valid():
    	    new_property = form.save()
    	    property_id = new_property.pk
    	else:
    		#TODO: display error message saying "invalid property details; please try again"
    		return HttpResponseRedirect('/report/property/search/')
	return property_id

def property_vendor_search(request):
	if request.method == 'POST':
	    property_id = get_or_create_property(request)
	    return HttpResponseRedirect('/report/property/%s/report_create/' % property_id)
	else:
		form = PropertyForm()
		context = {
			'form' : form
		}
    	return render(request, 'report/property_vendor_search.html', context)


def property_report_create(request, property_id):
	#TODO: retrieve user_id from logged in user session
	#user_id = request.user.id
	user_id = 1
	if request.method == 'POST':
		form = ReportForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			form.save()
			return HttpResponseRedirect('/report/evaluator/%s/report/list/' % user_id)
		else:
			raise ValidationError("Form has an invalid input")

	# if a GET (or any other method) we'll create a blank form
	else:
		form = ReportForm(initial={'property_id': property_id})
		context = {
			'form' : form
		}
    	return render(request, 'report/report_create.html', context)

def property_search(request):
	if request.method == 'POST':
	    property_id = get_or_create_property(request)
	    return HttpResponseRedirect('/report/property/%s/report_list/' % property_id)
	else:
		form = PropertyForm()
		context = {
			'form' : form
		}
    	return render(request, 'report/property_search.html', context)

def property_report_list(request, property_id):
	#TODO: check if db index is created on property_id field
	report_list = Report.objects.filter(property_id__exact=property_id)
	template = loader.get_template('report/report_list.html')
	context = {
	    'property_id': property_id
		'report_list': report_list,
	}
	return HttpResponse(template.render(context, request))

def property_report_request(request, property_id, report_id):
	#TODO: retrieve user_id from logged in user session
	#user_id = request.user.id
	user_id = 1
	if report_id:
	    form = ReportRequestForm(user_id=user_id, property_id=property_id, report_id=report_id)
    else:
    	# report_id = 0 => report yet to be created
	    form = ReportRequestForm(user_id=user_id, property_id=property_id)
	return HttpResponseRedirect('/report/user/%s/request_list/' % user_id)

def user_report_request_list(request, user_id):
	#TODO: check if db index is created on user_id field
	request_list = ReportRequest.objects.filter(user_id__exact=user_id)
	template = loader.get_template('report/user_report_request_list.html')
	context = {
		'request_list': request_list,
	}
	return HttpResponse(template.render(context, request))

def report_request_update(request, report_request_id):
	#TODO: retrieve user_id from logged in user session
	#user_id = request.user.id
	user_id = 1
	try:
		report_request = ReportRequest.objects.get(pk=report_request_id)
	except ReportRequest.DoesNotExist:
		raise Http404("Report Request does not exist")
	if request.method == 'POST':
		form = ReportRequestForm(request.POST, request.FILES, instance=report_request)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			form.save()
	        return HttpResponseRedirect('/report/user/%s/request_list/' % user_id)
   		else:
			raise ValidationError("Form has an invalid input")

	# if a GET (or any other method) we'll create a blank form
	else:
		form = ReportRequestForm(instance=report_request)
		context = {
			'report_request' : report_request,
			'form' : form
		}
		return render(request, 'report/report_request_update.html', context)
