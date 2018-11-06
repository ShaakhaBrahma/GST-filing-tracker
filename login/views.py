
from django.shortcuts import render,redirect
from .models import Client, R1a
from django.template import RequestContext
#from .forms import ClientEntry

# Create your views here.
def homepage(request):
    if request.method=="GET":
        return render(request, "homepage.html")
    if request.method == "POST":
        return render(request, 'homepage.html')
def about(request):
    if request.method=="GET":
        return render(request, "about.html")
def login1(request):
    if request.method=="GET":
        return render(request, "login1.html")
    if request.method == "POST":
        return redirect('login:index')


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
        return redirect('login:R1a', gstin=str(data.gstin))
    if request.method == "GET":
        return render(request, 'index.html')
def R1afill(request, gstin):
    if request.method=="POST":
            data = R1a()
            client = Client()
            client.gstin = gstin
            data.gstin = client
            data.igst = request.POST.get('igst')
            data.cess = request.POST.get('cess')
            data.month = request.POST.get('month')
            data.taxable_value = request.POST.get('taxable_value')
            data.cgst = request.POST.get('cgst')
            data.igst=request.POST.get('igst')
            data.total = request.POST.get('total')
            data.save()
            client.save()
            return render(request, 'R1a.html')
    if request.method == "GET":
        return render(request, 'R1a.html', context={'allgstin': gstin})





