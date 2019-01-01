from django.forms import ModelForm
from report.models import Evaluator, Report, User


class EvaluatorForm(ModelForm):
	class Meta:
		model = Evaluator
		fields = ['name', 'email', 'telephone', 'address']


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['name', 'email', 'telephone', 'address']


class ReportForm(ModelForm):
	class Meta:
		model = Report
		fields = ['evaluator_id', 'property_address']