
from django.shortcuts import render, redirect
from .models import Client, R1a, R2a, B3a
from django.template import RequestContext
from django.forms import ModelForm, forms
from django.db.models import signals
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import connection, transaction
#from .forms import ClientEntry

# Create your views here.
def homepage(request):
    if request.method=="GET":
        return render(request, "homepage.html")
    if request.method == "POST":
        return render(request, 'homepage.html')

def about(request):
    if request.method == "GET":
        return render(request, "about.html")

def login1(request):
    if request.method == "GET":
        return render(request, "login1.html")
    if request.method == "POST":
        return render(request, "index.html")


def index(request):
    if request.method == "POST":
        request_context = RequestContext(request)
        data = Client()
        data.name = request.POST.get('name')
        data.gstin = request.POST.get('gstin')
        data.phn = request.POST.get('phn')
        data.usr = request.POST.get('usr')
        data.passwd = request.POST.get('passwd')
        data.mail = request.POST.get('mail')
        data.pan = request.POST.get('pan')
        data.provisional_id = request.POST.get('provisional_id')
        data.save()

        return redirect('login:choice', gstin=str(data.gstin))
    if request.method == "GET":
        return render(request, 'index.html')

    def clean_username(self, gstin):
        user_model = get_user_model()  # your way of getting the User
        try:
            user_model.objects.get(username__iexact=gstin)
        except user_model.DoesNotExist:
            return gstin
        raise forms.ValidationError(_("This username has already existed."))

def clogin(request):
    if request.method =="POST":
        gstinl = request.POST.get('gstinl')
        return redirect('login:choice', gstin=str(gstinl))
    if request.method == "GET":
        return render(request, 'index.html')

def R1afill(request, gstin):
    if request.method == "POST":
            data = R1a()
            client = Client()
            client.gstin = gstin
            data.gstin = client
            data.igst = request.POST.get('igst')
            data.cess = request.POST.get('cess')
            data.month = request.POST.get('month')
            data.sgst = request.POST.get('sgst')
            data.taxable_value = request.POST.get('taxable_value')
            data.cgst = request.POST.get('cgst')
            data.igst=request.POST.get('igst')
            data.total = request.POST.get('total')
            data.save()
            client.save()
            return render(request, 'R1afill.html', context={'allgstin': gstin})
    if request.method == "GET":
        #return HttpResponseRedirect(reverse('login:R1afill', args=(gstin)))
        return render(request, 'R1afill.html', context={'allgstin': gstin})

def choice(request, gstin):
    if request.method == "GET":
        return render(request, 'choice.html', context={'allgstin': gstin})

    if request.method == "POST":
        return render(request, 'choice.html', context={'allgstin': gstin})

def R2afill(request, gstin):
    if request.method == "POST":
        r2a = R2a()
        r2 = Client()
        r2.gstin = gstin
        r2a.gstin = r2
        r2a.igst = request.POST.get('igst')
        r2a.sgst = request.POST.get('sgst')
        r2a.cgst = request.POST.get('cgst')
        r2a.month = request.POST.get('month')
        r2a.cess = request.POST.get('cess')
        r2a.taxable_value=request.POST.get('taxable_value')
        r2a.total = request.POST.get('total')
        r2.save()
        r2a.save()

        return render(request, 'R2afill.html', context={'allgstin': gstin})
    if request.method == "GET":
        return render(request, 'R2afill.html', context={'allgstin': gstin})

def B3afill(request, gstin):
    if request.method == "POST":
        r3 = Client()
        b3a = B3a()
        r3.gstin = gstin
        b3a.gstin = r3
        b3a.ty = request.POST.get('ty')
        b3a.month = request.POST.get('month')
        b3a.taxable_value = request.POST.get('taxable_value')
        b3a.total = request.POST.get('total')
        b3a.igst = request.POST.get('igst')
        r3.save()
        b3a.save()

        return render(request, 'B3afill.html', context={'allgstin': gstin})
    if request.method == "GET":
        return render(request, 'B3afill.html', context={'allgstin': gstin})

def status(request):
    if request.method == "POST":
        gst = request.POST.get('gstin')
        allclients = Client.objects.raw('select * from login_client')
        r1a = R1a.objects.filter(gstin=gst)
        r2a = R2a.objects.filter(gstin=gst)
        b3a = B3a.objects.filter(gstin=gst)
        return render(request, 'status.html', context={'allclients': allclients, 'r1a': r1a, 'r2a': r2a, 'b3a': b3a})
    if request.method == "GET":
        allclients = Client.objects.raw('select * from login_client')
        return render(request, 'status.html', context={'allclients': allclients})


