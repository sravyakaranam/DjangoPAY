from django.shortcuts import render,redirect
from products.models import Watch,Phone,Laptop,Product
from django.http import HttpResponse,response,HttpResponseRedirect
from products.forms import LaptopForm,WatchForm,PhoneForm,ProductForm
from django.contrib import messages
from accounts.models import Account
import os

# Create your views here.
message='Added to cart Successfully'
myproducts={}

amt=0
cnt=1
def view_products(request,id=None):
    form=None
    form=LaptopForm(request.GET)
    Lapi=Laptop.objects.all()
    phn=Phone.objects.all()
    Wth=Watch.objects.all()
  
    return render(request,'forms.html',{'form':form,'Lapi':Lapi,'phn':phn,'Wth':Wth,'message':message})

def add(self, key, value): 
        self[key] = value 
    
def addtocart(request,id=None):
    flag=0
    form=None
    z=None
    
    try:
        lapi=Laptop.objects.get(id=id)
        # lst=Laptop.objects.all()
        for x in myproducts.keys():
            if (x.id == lapi.id):
                flag=1
                cnt = myproducts.get(x)
                cnt=int(cnt)
                myproducts[lapi]=cnt+1
                amt+=lapi.cost
        if flag==0:
            myproducts[lapi]=1
            amt+=lapi.cost
        # msg='Laptop' + ' ' + lapi.name + ' ' +id + ' Added successfully'
        # return render(request,'forms.html',{'obj':lapi,'msg':msg,'myproducts':myproducts})

    except:
        try:
            wth=Watch.objects.get(id=id)
            for x in myproducts.keys():
                if(x.id == wth.id):
                    flag=1
                    cnt = myproducts.get(x)
                    cnt=int(cnt)
                    myproducts[wth]=cnt+1
                    amt+=lapi.cost
            if flag==0:
                myproducts[wth]=1
                amt+=lapi.cost
            # msg='Watch ' + wth.name + ' '+id + ' Added successfully'
            # return render(request,'forms.html',{'obj':wth,'msg':msg,'myproducts':myproducts})
        except:
            try:
    
                phn=Phone.objects.get(id=id)
                for x in myproducts.keys():
                    if (x.id == phn.id):
                        flag=1
                        cnt = myproducts.get(x)
                        cnt=int(cnt)
                        myproducts[phn]=cnt+1
                        amt+=lapi.cost
                if flag==0:
                    myproducts[phn]=1
                    amt+=lapi.cost
                # return render(request,'forms.html',{'obj':phn,'msg':msg,'myproducts':myproducts})
            except:
                pass
    print('myprod')
    print(myproducts)
    messages.success(request, 'Your password was updated successfully!')
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/added'))
    # return render(request,'viewcart.html',{'form':form,'cnt':cnt,'myproducts':myproducts})



def viewcart(request):
    lst1=Product.objects.all()
    lst2=Laptop.objects.all()
    
    for x in lst1:
        for y in lst2:
            try:
                xas=x.name
                yas=y.name
                print(xas)
                print(yas)
                obj=Laptop.objects.get(xas=yas)
               
                key=obj
                value=x.items
                myproducts.add(key,value)
            except:
                try:
                    xas=x.name
                    yas=y.name
                    print(xas)
                    print(yas)
                    obj=Laptop.objects.get(xas=yas)
                    key=obj
                    value=x.items
                    myproducts.add(key,value)
                except:
                    try:
                        xas=x.name
                        yas=y.name
                        print(xas)
                        print(yas)
                        obj=Laptop.objects.get(xas=yas)
                        key=obj
                        value=x.items
                        myproducts.add(key,value)
                    except:
                        pass
    form=None
    amt=0
    lst=myproducts.keys()
    for x,y in myproducts.items():
        amt+=(x.cost)*y

    return render(request,'viewcart.html',{'form':form,'myproducts':myproducts,'lst':lst,'amt':amt})


def deleteproduct(request,id):
    ltop=[]
    flag=0
    myp=[]
    amt=0
    for x,y in myproducts.items():
        amt+=(x.cost)*y
    
    try:
        
        lapi=Laptop.objects.get(id=id)
        ltop=Laptop.objects.all()
     
        for key,value in myproducts.items():
            if (key==lapi):
                if value==1:
                    amt-=key.cost
                    del myproducts[lapi]
                else:
                    myproducts[key] = myproducts[key]-1
                    amt-=key.cost
    except:
        try:
            
            wth=Watch.objects.get(id=id)
            ltop=Watch.objects.all()
        
            for key,value in myproducts.items():
                if (key==wth):
                    if value==1:
                        amt-=key.cost
                        del myproducts[wth]
                    else:
                        myproducts[key] = myproducts[key]-1
                        amt-=key.cost
        except:
            try:
                phn=Phone.objects.get(id=id)
                ltop=Phone.objects.all()
            
                for key,value in myproducts.items():
                    if (key==phn):
                        if value==1:
                            del myproducts[phn]
                            amt-=key.cost
                        else:
                            myproducts[key] = myproducts[key]-1
                            amt-=key.cost
            except:
                pass
                        
    return render(request,'viewcart.html',{'myproducts':myproducts,'amt':amt})

def buynow(request,id):
    obj=''
    ltop=[]
    flag=0
    myp=[]
    amt=0
  
    for x,y in myproducts.items():
        amt+=(x.cost)*y
        

    obj=Account.objects.all()
    for x in obj:
        x.balance-=amt
    
    x.save()
    try:
        lapi=Laptop.objects.get(id=id)
        ltop=Laptop.objects.all()
        return render(request,'buynow.html',{'bal':x.balance,'company':lapi.company,'cost':lapi.cost})     
    except:
        try:
            wth=Watch.objects.get(id=id)
            ltop=Watch.objects.all()
            return render(request,'buynow.html',{'bal':x.balance,'company':wth.company,'cost':wth.cost})    
        except:
            try:
                phn=Phone.objects.get(id=id)
                ltop=Phone.objects.all()
                return render(request,'buynow.html',{'bal':x.balance,'company':wth.company,'cost':wth.cost})   
            except:
                return ''

def savetodb(request):
    msg=''
    form=''
    print('hunny')
    for x,y in myproducts.items():
        print('sravya')
        product=Product(
                    name=x.name,
                    company=x.company,
                    cost=x.cost,
                    items=y)
        print(x.name)
        product.save()
    print('harshi')

    
    return redirect('/')