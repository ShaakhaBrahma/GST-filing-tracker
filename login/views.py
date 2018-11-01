from django.shortcuts import render
from .models import Client,R1a
from .forms import ClientEntry

# Create your views here.
def index(request):
	if request.method=="GET":
		cform=ClientEntry()
		#pass
		#context={'animals':Animal.objects.all(),}
		return render(request,'index.html',{'cform':cform})


	if request.method=="POST":

		instance = ClientEntry(request.POST)
		instance.save()

		context={'clients':Client.objects.all()}
		return render(request,'index.html',context)
		