from django.forms import ModelForm
from report.models import Evaluator, Report, User
#form class
class EvaluatorForm(ModelForm):
	class Meta:
		model = Evaluator
		fields = ['name', 'email', 'telephone', 'address']

#create form to add an evaluator
form = EvaluatorForm()

#create form to change an existing evaluator
#evaluator = Evaluator.objects.get(pk=1)
#form = EvaluatorForm(instance=evaluator)

