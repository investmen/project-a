from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField, FileField, ForeignKey
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
#from django.core import validators

#EXTENSIONS = [validators.FileExtensionValidator(allowed_extensions=['pdf','jpg'])]

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
	#phone = IntegerField(null=True)
	#company_name = CharField(max_length=200, null=True)
	## bank user fields
	#location = CharField(max_length = 200, null=True)
	## evaluator user fields
	#company_address = CharField(max_length=200, null=True)
	#aadhaar_number = IntegerField(null=True)
	#pan = IntegerField(null=True)
	#cin = IntegerField(null=True)
	#supporting_docs = FileField(upload_to='supporting_docs/', validators=EXTENSIONS, blank=True, null=True)
	#payment_info = ForeignKey(PaymentInfo, on_delete=models.CASCADE, null=True)
	#VALID_STATUSES = (
	#	('Inactive', 'Inactive'),
	#	('Registration-in-progress', 'Registration-in-progress'),
	#	('Registered', 'Registered'),
	#	('Rejected', 'Rejected')
	#)
	#status = CharField(choices=VALID_STATUSES, max_length=200, default='Inactive', null=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
