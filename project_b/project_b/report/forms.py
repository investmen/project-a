from django.forms import ModelForm, CharField
from django.contrib.postgres.forms import JSONField
from project_b.report.models import PaymentInfo, Evaluator, Property, Report, User, ReportRequest


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

class ReportUpdateForm(ModelForm):
	#evaluator = forms.ModelChoiceField(queryset=Evaluator.objects.all())
	#proprty = forms.ModelChoiceField(queryset=Property.objects.all())
	class Meta:
		model = Report 
		#exclude = ["report_json"]
		exclude = []

	def __init__(self, *args, **kwargs):
		report = kwargs.pop('extra')
		super(ReportUpdateForm, self).__init__(*args, **kwargs)
		report_json = report.report_json
		for i, k in enumerate(report_json.keys()):
			self.fields['field_%s' % i] = CharField(label=k, initial=report_json[k])

	def extra_fields(self):
		for name, value in self.cleaned_data.items():
			if name.startswith('field_'):
				yield (self.fields[name].label, value)

	def clear_extra_fields(self):
		for name in list(self.cleaned_data):
			if name.startswith('field_'):
				del self.cleaned_data[name]

class ReportRequestDownloadableForm(ModelForm):
	class Meta:
		model = ReportRequest
		exclude = []


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        exclude = []

class ReportForm(ModelForm):
    class Meta:
        model = Report
        exclude = []

