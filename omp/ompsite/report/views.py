from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.core.exceptions import ValidationError
from .models import Evaluator, Report, User
from .forms import EvaluatorForm, ReportRequestForm, ReportCompleteForm, UserForm



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
	
