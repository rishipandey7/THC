from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product,Contact,Order,OrderUpdate
from math import ceil
from django.contrib.auth.models import User,auth
from django.contrib import messages
import json


def home(request):

    allProds = []
    catproduct = Product.objects.values('category')
    cats = {item['category'] for item in catproduct}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        no_of_slides = n//4 + ceil((n/4) + (n//4))
        allProds.append([prod,range(1,no_of_slides),no_of_slides])

    params={'allProds':allProds }
    return render(request,'shop/home.html',params)



def about(request):
    
    return render(request,'shop/about.html')



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')

        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    
    return render(request,'shop/contact.html')
    
def tracker(request):
    # updates = []
    # if request.method=="POST":
    #     orderId = request.POST.get('orderId', '')
    #     email = request.POST.get('email', '')
    #     update = OrderUpdate.objects.filter(order_id=orderId)
        
    #     updates.append({'text': item.update_desc, 'time': item.timestamp})

    # params={'allProds':updates }
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')
    
def updatetracker(request):
    
    updates = {}
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        update = OrderUpdate.objects.filter(order_id=orderId)

        for item in update:
            UpdateDict = {'text': item.update_desc, 'time': item.timestamp}
            updates.update(UpdateDict)


    # params={'allProds':updates}
    return render(request,'shop/updatetracker.html',updates)

def productview(request,myid):
    product=Product.objects.filter(id=myid)

    return render(request,'shop/productview.html', {'product':product[0]})



def checkout(request):

    if request.method == "POST":

        item_json = request.POST.get('item_json','')
        name = request.POST.get('name','')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email','')
        address = request.POST.get('address1','') + ' ' + request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        phone = request.POST.get('phone','')
        zip_code = request.POST.get('zip_code','')

        order = Order(item_json=item_json, name=name, email=email, address=address, city =city , state=state, phone=phone,zip_code=zip_code,amount=amount)
        order.save()
        update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = Order.order_id
        return render(request,'shop/checkout.html', {'thank' :thank,'id':id})
    return render(request,'shop/checkout.html')    

def signup(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username=name,email=email,password=password)
        myuser.save()

        messages.success(request,"Your account has been succesfully created ")
        return redirect('login')

    return render(request,'shop/signup.html')

def login(request):

    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=name,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/shop')
        else:
            messages.info(request,'invalid login attempt')
            return redirect('login')


    return render(request,'shop/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/shop')