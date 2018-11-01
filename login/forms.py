from django.forms import ModelForm
from .models import *



class ClientEntry(ModelForm):

	class Meta:
		model=Client
		fields='__all__'
		
			
