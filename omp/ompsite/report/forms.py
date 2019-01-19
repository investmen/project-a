from django.forms import ModelForm
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
		fields = ['evaluator', 'report']

class PropertyForm(ModelForm):
	class Meta:
		model = Property
		exclude = []

class ReportForm(ModelForm):
	class Meta:
		model = Report
		exclude = []

class ReportRequestDownloadableForm(ModelForm):
	class Meta:
		model = ReportRequest
		exclude = []

