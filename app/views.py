from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_data(request):
    form=NameForm()
    d={'form':form}
    if request.method=='POST':
        fd=NameForm(request.POST)
        if fd.is_valid():
            name=fd.cleaned_data['name']
            age=fd.cleaned_data['age']
            email=fd.cleaned_data['email']
            pw=fd.cleaned_data['password']
            addr=fd.cleaned_data['address']
            gen=fd.cleaned_data['gender']
            cou=fd.cleaned_data['courses']
            F=Name.objects.get_or_create(name=name,age=age,email=email,password=pw,address=addr,gender=gen,course=cou)[0]
            F.save()

            FO=Name.objects.all()
            d1={'FO':FO}
            return render(request,'display_students.html',d1)
            
    return render(request,'insert_data.html',d)