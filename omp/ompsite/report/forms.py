from django.forms import ModelForm
from django.contrib.postgres.forms import JSONField
from report.models import PaymentInfo, Evaluator, Property, Report, User, ReportRequest


class PaymentInfoForm(ModelForm):
	class Meta:
		model = PaymentInfo
		exclude = []

class EvaluatorForm(ModelForm):
	class Meta:
		model = Evaluator
		exclude = ['payment_info']


class UserForm(ModelForm):
	class Meta:
		model = User
		exclude = []

class ReportRequestForm(ModelForm):
	class Meta:
		model = ReportRequest
		exclude = []

class ReportCompleteForm(ModelForm):
	class Meta:
		model = Report
		fields = ['evaluator']

class PropertyForm(ModelForm):
	class Meta:
		model = Property
		exclude = []

class ReportForm(ModelForm):
	class Meta:
		model = Report
		exclude = []

class ReportUpdateForm(ModelForm):
	#evaluator = forms.ModelChoiceField(queryset=Evaluator.objects.all())
	#proprty = forms.ModelChoiceField(queryset=Property.objects.all())
	class Meta:
		model = Report 
		exclude = ["report_json"]

	def __init__(self, *args, **kwargs):
		report = kwargs.pop('extra')
		super(ReportUpdateForm, self).__init__(*args, **kwargs)
		report_json = report.report_json
		for i, k in enumerate(report_json.keys()):
			self.fields['field_%s' % i] = JSONField(label=k, initial=report_json[k])


class ReportRequestDownloadableForm(ModelForm):
	class Meta:
		model = ReportRequest
		exclude = []

