from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.core.exceptions import ValidationError
from .models import Evaluator, Property, Report, User, ReportRequest
from .forms import PaymentInfoForm, EvaluatorForm, PropertyForm, ReportForm, ReportUpdateForm, ReportRequestForm, ReportCompleteForm, UserForm



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
            #TODO: replace all hardcoded 'url' with url names from urls.py
            return HttpResponseRedirect('/report/evaluator/list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EvaluatorForm()
        context = {
            'form' : form
        }
    #TODO: see if you can replace hardcoded file paths with some names similar to url names
    return render(request, 'report/evaluator_create.html', context)
    
def evaluator_update(request, evaluator_id):
    try:
        evaluator = Evaluator.objects.get(pk=evaluator_id)
    except Report.DoesNotExist:
        raise Http404("Evaluator does not exist")
    if request.method == 'POST':
        form = EvaluatorForm(request.POST, request.FILES, instance=evaluator)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/report/evaluator/%s/dashboard/' % evaluator_id)
        else:
            raise ValidationError("Form has an invalid input")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EvaluatorForm(instance=evaluator)
        context = {
            'evaluator' : evaluator,
            'form' : form
        }
        return render(request, 'report/evaluator_update.html', context)

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
        form = ReportUpdateForm(request.POST, instance=report, extra=report)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #form.cleaned_data["report_json"] = {}
            i = 0
            for (field, value) in form.extra_fields('field_'):
                # the variable field contains the section titles like 'Instruction', 'Fair Market Value Analysis'...  
                d = {}
                # now lets iterate through the fields within a section
                for (field, value) in form.extra_fields('field_%s_' % i):
                    d[field] = value
                form.cleaned_data["report_json"][field] = d

            #form.clear_extra_fields()
            form.save()
            #model = Report(**form.cleaned_data)
            #model.save()
            return HttpResponseRedirect('/report/report/list/')
        else:
            raise ValidationError("Form has an invalid input")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReportUpdateForm(instance=report, extra=report)
        context = {
            'report' : report,
            'form' : form
        }
        return render(request, 'report/report_update.html', context)
 
def get_or_create_property(request):
    form = PropertyForm(request.POST)
    if form.is_valid():
        pincode = form.cleaned_data['pincode']
        locality = form.cleaned_data['locality']
        name = form.cleaned_data['name']
        try:
            #TODO: check if db index is created on search fields
            properties = Property.objects.filter(pincode__exact=pincode, locality__contains=locality, name__contains=name)
            #TODO: handle multiple property matches
            property_id = properties[0].id
        except (Property.DoesNotExist, IndexError) as e:
            new_property = form.save()
            property_id = new_property.pk
    else:
        #TODO: display error message saying "invalid property details; please try again"
        return HttpResponseRedirect('/report/property/search/')
    return property_id

def property_evaluator_search(request):
    if request.method == 'POST':
        property_id = get_or_create_property(request)
        return HttpResponseRedirect('/report/property/%s/report_create/' % property_id)
    else:
        form = PropertyForm()
        context = {
            'form' : form
        }
        return render(request, 'report/property_evaluator_search.html', context)


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
            return HttpResponseRedirect('/report/evaluator/%s/report_list/' % user_id)
        else:
            raise ValidationError("Form has an invalid input")

    # if a GET (or any other method) we'll create a blank form
    else:
        try:
            property = Property.objects.get(pk=property_id)
        except Property.DoesNotExist:
            raise Http404("Property does not exist")
        form = ReportForm(initial={'property': property})
        context = {
            'form' : form,
            'property_id': property_id
        }
        return render(request, 'report/report_create.html', context)

def evaluator_report_list(request, evaluator_id):
    #TODO: check if db index is created on user_id field
    report_list = Report.objects.filter(evaluator=evaluator_id)
    template = loader.get_template('report/evaluator_report_list.html')
    context = {
        'report_list': report_list,
    }
    return HttpResponse(template.render(context, request))

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
    report_list = Report.objects.filter(property=property_id)
    #print("report_list", report_list)
    #report_evaluator_tuple = tuple(report.evaluator.id for report in report_list)
    #print("report_evaluator_tuple", report_evaluator_tuple)
    #evaluator_sample_report_map = {evaluator.id:evaluator.sample_report 
    #                               for evaluator in Evaluator.objects.filter(id__in=report_evaluator_tuple)}
    #print(evaluator_sample_report_map)
    #sample_report_list = [ReportForm(instance=Report(report.evaluator, report.property, evaluator_sample_report_map[report.evaluator.id]))
    #                      for report in report_list]
    for report in report_list:
        report.report = report.evaluator.sample_report
    #print("report_list", report_list)
    #print([form.fields for form in sample_report_list])
    template = loader.get_template('report/property_report_list.html')
    context = {
        'property_id': property_id,
        'report_list': [(report.id, ReportForm(instance=report)) for report in report_list],
        #'report_list': sample_report_list,
    }
    return HttpResponse(template.render(context, request))

def property_report_request(request, property_id, report_id):
    #TODO: retrieve user_id from logged in user session
    #user_id = request.user.id
    user_id = 1
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    if report_id:
        try:
            report = Report.objects.get(pk=report_id)
        except Report.DoesNotExist:
            raise Http404("Report does not exist")
        model = ReportRequest(user=user, report=report)
    else:
        # report_id = 0 => report yet to be created
        model = ReportRequest(user=user)
    model.save()
    print("report request created with id: %s" % model.id)
    #TODO: display success message with request id in request_list page
    return HttpResponseRedirect('/report/user/%s/report_request_list/' % user_id)

def report_request_list(request):
    request_list = ReportRequest.objects.all()
    template = loader.get_template('report/report_request_list.html')
    context = {
        'request_list': request_list,
    }
    return HttpResponse(template.render(context, request))

def user_report_request_list(request, user_id):
    #TODO: check if db index is created on user_id field
    request_list = ReportRequest.objects.filter(user=user_id)
    """
    for request in request_list:
        if request.status != 'Ready to Download Report':
            original_report = request.report
            file_hidden_report = 

    report_request_map = {request.report_id:request.id if request.report_id for request in request_list}
    #TODO: see if two(above and below) can be combined into one by joins
    report_list = Report.objects.filter(id__in=report_request_map.keys())
    #display report file only if report is in ready for download status
    downloadable_report_requests = [(report_request_map[report.id].id, report) if report_request_map[report.id].status == 'Ready to Download Report'
                                    else (report_request_map[report.id].id, Report(report.evaluator_id, report.property_id))
                                    for report in report_list]
    context = {
        'request_list': downloadable_report_requests,
    }
    """
    context = {
        'request_list': request_list,
    }
    template = loader.get_template('report/user_report_request_list.html')
    return HttpResponse(template.render(context, request))

def report_request_update(request, report_request_id, is_evaluator=None):
    #TODO: retrieve user_id from logged in user session
    #user_id = request.user.id
    user_id = 1
    try:
        report_request = ReportRequest.objects.get(pk=report_request_id)
    except ReportRequest.DoesNotExist:
        raise Http404("Report Request does not exist")
    if request.method == 'POST':
        update_allowed = False
        if is_evaluator == 1 or is_evaluator is None:
            update_allowed = True
        else:
            # user should not be able to update report status to 'Ready to download' before payment
            for status in ReportRequest.ALLOWED_STATES_FOR_USER:
                if report_request.status in status:
                    update_allowed = True
                    break
        if update_allowed:
            form = ReportRequestForm(request.POST, request.FILES, instance=report_request)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                form.save()
                if is_evaluator == 1 or is_evaluator is None:
                    #TODO: use report_request.report.evaluator_id
                    return HttpResponseRedirect('/report/evaluator/%s/report_request_list/' % 1)
                else:
                    return HttpResponseRedirect('/report/user/%s/report_request_list/' % user_id)
            else:
                raise ValidationError("Form has an invalid input")
        else:
            raise Http404("Permission denied to update request")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReportRequestForm(instance=report_request)
        context = {
            'report_request' : report_request,
            'form' : form
        }
        return render(request, 'report/report_request_update.html', context)

def evaluator_report_request_list(request, evaluator_id):
    #TODO: check if db index is created on user_id field
    request_list = ReportRequest.objects.select_related('report').filter(report__evaluator_id=evaluator_id)
    template = loader.get_template('report/evaluator_report_request_list.html')
    context = {
        'request_list': request_list,
    }
    return HttpResponse(template.render(context, request))

def payment_info_create(request, evaluator_id):
    if request.method == 'POST':
        form = PaymentInfoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            new_payment_info = form.save()
            payment_info_id = new_payment_info.pk
            try:
                evaluator = Evaluator.objects.get(pk=evaluator_id)
            except Evaluator.DoesNotExist:
                raise Http404("Evaluator does not exist")
            evaluator_form  = EvaluatorForm(payment_info_id=payment_info_id, instance=evaluator)
            evaluator_form.save()
            return HttpResponseRedirect('/report/evaluator/%s/' % evaluator_id)
        else:
            raise ValidationError("Form has an invalid input")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PaymentInfoForm()
        context = {
            'form' : form
        }

    return render(request, 'report/payment_info_create.html', context)
    
def payment_info_update(request, evaluator_id, payment_info_id):
    try:
        payment_info = PaymentInfo.objects.get(pk=payment_info_id)
    except PaymentInfo.DoesNotExist:
        raise Http404("PaymentInfo does not exist")
    if request.method == 'POST':
        form = PaymentInfoForm(request.POST, instance=payment_info)
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
        form = PaymentInfoForm(instance=payment_info)
        context = {
            'payment_info' : payment_info,
            'form' : form
        }
        return render(request, 'report/payment_info_update.html', context)
    
def evaluator_dashboard(request, evaluator_id):
    context = {'evaluator_id': evaluator_id}
    return render(request, 'report/evaluator_dashboard.html', context)

def user_dashboard(request, user_id):
    context = {'user_id': user_id}
    return render(request, 'report/user_dashboard.html', context)

def admin_dashboard(request):
    context = {}
    return render(request, 'report/admin_dashboard.html', context)

