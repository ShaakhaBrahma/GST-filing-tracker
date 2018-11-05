from django.forms import ModelForm
from .models import *



class ClientEntry(ModelForm):

	class Meta:
		model=Client
		fields='__all__'
		allgstin = forms.ModelChoiceField(queryset=Client.objects.all)

		

