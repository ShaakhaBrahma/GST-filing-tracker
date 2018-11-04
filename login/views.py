
from django.shortcuts import render
from .models import Client, R1a
from django.template import RequestContext
#from .forms import ClientEntry

# Create your views here.
def homepage(request):
    if request.method=="GET":
        return render(request, "homepage.html")
    if request.method == "POST":
        return render(request, 'homepage.html')

def index(request):
    if request.method=="POST":
        request_context = RequestContext(request)
        data = Client()
        data.gstin = request.POST.get('gstin')
        data.phn = request.POST.get('phn')
        data.usr = request.POST.get('usr')
        data.passwd = request.POST.get('passwd')
        data.mail = request.POST.get('mail')
        data.pan = request.POST.get('pan')
        data.save()
        return render(request, 'index.html')
    if request.method == "GET":
        return render(request, 'index.html')


