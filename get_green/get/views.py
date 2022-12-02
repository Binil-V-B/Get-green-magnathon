from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import pro,rank
# Create your views here.

def first(request):
        return render(request,'index.html')

def home(request):
    list=rank.objects.all().order_by('-amount')
    return render(request,'home.html',{'name':list})

def sell(request):
    return render(request,'sell.html')
def action(request):
    
    product =request.POST['name']
    contact = request.POST['cont']
    type=request.POST['option']

    pro.objects.create(name=product,co_non=contact,type=type)
    return HttpResponse("product added")
    
def buy(request):
    products_list=pro.objects.all()
    return render(request,'buy.html',{'prod':products_list})

def invest(request):
    return render(request,'invest.html')

def report(request):
    return render(request,'report.html')

def clean(request):
    return render(request,'clean.html')

def buy1(request):
    return render(request,'buy.html')

def buyorsell(request):
    return render(request,'buyorsell.html')

def sell1(request):
    return render(request,'sell.html')

def orr(request):
    return render(request,'orientation.html')

def map(request):
    return render(request,'map.html')

def sub(request):
    name=request.POST['name']
    amount=request.POST['amount']
    rank.objects.create(name=name,amount=amount)
    return render(request,"confirm.html")

def con(request):
    return render(request,'confirm2.html')