from django.forms import ModelForm
from report.models import PaymentInfo, Evaluator, Property, Report, User, ReportRequest


class EvaluatorForm(ModelForm):
	class Meta:
		model = Evaluator
		exclude = ['name', 'email', 'phone', 'company_address']


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['name', 'email', 'phone']

class ReportRequestForm(ModelForm):
	class Meta:
		model = Report
		fields = ['evaluator_id']

class ReportCompleteForm(ModelForm):
	class Meta:
		model = Report
		fields = ['evaluator_id', 'report']

#class PropertyForm(ModelForm):
#	class Meta:
#		model = Property