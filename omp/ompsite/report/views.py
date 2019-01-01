from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import Evaluator
from .forms import EvaluatorForm



def index(request):
	return HttpResponse("Hello..You are at the Report app index.")

def list_evaluator(request):
	evaluator_list = Evaluator.objects.all()
	template = loader.get_template('report/index.html')
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