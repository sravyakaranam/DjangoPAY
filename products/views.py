from django.shortcuts import render,redirect
from products.models import Watch,Phone,Laptop,Table
from django.http import HttpResponse,response,HttpResponseRedirect
from products.forms import LaptopForm,WatchForm,PhoneForm,ProductForm
from django.contrib import messages
from accounts.models import Account
import os
from django.contrib.auth.models import User
from django.contrib import messages

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
    table=Table()
    z=None
    try:
        lapi=Laptop.objects.get(id=id)
        for x in myproducts.keys():
            if (x.id == lapi.id):
                flag=1
                cnt = myproducts.get(x)
                cnt=int(cnt)
                myproducts[lapi]=cnt+1
                table=Table.objects.create(
                    name=request.user,
                    pro_id=lapi.id
                )
                amt=amt+lapi.cost
        if flag==0:
            myproducts[lapi]=1
            
            table=Table()
            table=Table.objects.create(
                    name=request.user,
                    pro_id=lapi.id
                )
            amt=amt+lapi.cost
        

    except:
        try:
            wth=Watch.objects.get(id=id)
            for x in myproducts.keys():
                if(x.id == wth.id):
                    flag=1
                    cnt = myproducts.get(x)
                    cnt=int(cnt)
                    myproducts[wth]=cnt+1
                    
                    table=Table.objects.create(
                    name=request.user,
                    pro_id=wth.id
                    )
              
                    amt=amt+wth.cost
                    
                    
            if flag==0:
                myproducts[wth]=1
                
                table=Table.objects.create(
                    name=request.user,
                    pro_id=wth.id
                    )
                amt=amt+wth.cost
          
        except:
            try:
    
                phn=Phone.objects.get(id=id)
                for x in myproducts.keys():
                    if (x.id == phn.id):
                        flag=1
                        cnt = myproducts.get(x)
                        cnt=int(cnt)
                        myproducts[phn]=cnt+1
                     
                        table=Table.objects.create(
                        name=request.user,
                        pro_id=phn.id
                        )
                       
                        amt=amt+phn.cost
                    
                    
                if flag==0:
                    myproducts[phn]=1
                    
                    table=Table.objects.create(
                    name=request.user,
                    pro_id=phn.id
                    )
                    amt=amt+phn.cost
                   

                # return render(request,'forms.html',{'obj':phn,'msg':msg,'myproducts':myproducts})
            except:
                pass
  
  
    return redirect('/proview')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/added'))
    # return render(request,'viewcart.html',{'form':form,'cnt':cnt,'myproducts':myproducts})



def viewcart(request):
    lst2=Laptop.objects.all()
    lst1=myproducts.items()
    for x in lst1:
        for y in lst2:
            try:
                xas=x.name
                yas=y.name
                obj=Laptop.objects.get(xas=yas)
               
                key=obj
                value=x.items
                myproducts.add(key,value)
            except:
                try:
                    xas=x.name
                    yas=y.name
                    obj=Laptop.objects.get(xas=yas)
                    key=obj
                    value=x.items
                    myproducts.add(key,value)
                except:
                    try:
                        xas=x.name
                        yas=y.name
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
    msg=''
    quantity=1
    allusers=Account.objects.all()
    user = Account.objects.get(AccountUser=request.user)
    try:
        lapi=Laptop.objects.get(id=id)
        for x,y in myproducts.items():
            if(x.id == lapi.id):
                quantity=y
        for z in allusers:
            if (z==user):
                if(z.balance<lapi.cost):
                        msg="Sorry!! "+user.AccountUser+" Your balance is not sufficent to buy this product :("
                        return render(request,'buynow.html',{'bal':z.balance,'company':lapi.company,'cost':lapi.cost,'user':user,'msg':msg})    
                else:
                    z.balance-=(lapi.cost)*quantity
                    z.save()
        return render(request,'buynow.html',{'bal':z.balance,'company':lapi.company,'cost':lapi.cost,'user':user,'msg':msg})     
    except:
        try:
            wth=Watch.objects.get(id=id)
            for x,y in myproducts.items():
                if (x.id ==wth.id):
                    quantity=y
            for z in allusers:
                if (z==user):
                    if(z.balance<wth.cost):
                        msg="Sorry!! "+user.AccountUser+" Your balance is not sufficent to buy this product :("
                    else:
                        z.balance-=wth.cost*quantity
                        z.save()
            return render(request,'buynow.html',{'bal':z.balance,'company':wth.company,'cost':wth.cost,'user':user,'msg':msg})    
        except:
            try:
                phn=Phone.objects.get(id=id)
                ltop=Phone.objects.all()
                for x,y in myproducts.items():
                    if(x.id == phn.id):
                        quantity=y
                for z in allusers:
                    if (z==user):
                        if(z.balance<phn.cost):
                            msg="Sorry!! "+user.AccountUser+"Your balance is not sufficent to buy this product :("
                    else:
                        z.balance-=phn.cost*quantity
                        z.save()
                return render(request,'buynow.html',{'bal':z.balance,'company':phn.company,'cost':phn,'user':user,'msg':msg})   
            except:
                return ''


def load(request):
    name=request.user
    obj=[]
    account=[]
    acc=''
    users=''
    users = User.objects.get(username=request.user)

    obj=Table.objects.filter(name=request.user)
 
    for x in obj:
        addtocart(users.id,x.pro_id)
    return redirect('/proview')
