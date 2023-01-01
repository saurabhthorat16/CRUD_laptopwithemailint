from django.shortcuts import render, redirect
from .forms import LaptopForm
from .models import Laptop
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def laptopFormView(request):
    form = LaptopForm()
    template_name = 'CRUDAPP/laptopform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('showlaptop_url')
    return render(request, template_name,context)

@login_required()
def showlaptopView(request):
    obj = Laptop.objects.all()
    template_name = 'CRUDAPP/showlaptop.html'
    context = {'data': obj}
    return render(request, template_name, context)

def updateLaptopView(request, id):
    obj = Laptop.objects.get(id=id)
    form = LaptopForm(instance=obj)
    template_name = 'CRUDAPP/laptopform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        return redirect('showlaptop_url')
    return render(request, template_name, context)

def deleteLaptopView(request, id):
    obj = Laptop.objects.get(id=id)
    template_name = 'CRUDAPP/confirmation.html'
    context = {'data': obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('showlaptop_url')
    return render(request, template_name, context)
