from django.shortcuts import render
from .forms import contactFrom

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def djangoForm(request):
    form=contactFrom(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,'djangofrom.html',{'form':form})
