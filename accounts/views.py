from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomForms,Userform,SearchForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login,authenticate
from .models import Account
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


present=''

def profile(request):
    user=''
    msg=""
    if request.method == "POST":
        amount=''
        Requiredamount=''
        try:
            username = request.POST["username"]
            try:
                amount = request.POST["amount"]
            except:
                Requiredamount=request.POST["Requiredamount"]
            if(amount):

                senderUser = Account.objects.get(AccountUser=request.user.username)
                receiverrUser =  Account.objects.get(AccountUser=username)
                senderUser.balance = senderUser.balance - int(amount)
                receiverrUser.balance = receiverrUser.balance + int(amount)
                obj=User.objects.get(username=receiverrUser)
                senderUser.save()
                receiverrUser.save()
                msg = "Transaction Success"
                subject = ' Received money from '+ senderUser.AccountUser
                message = ' Hi '+receiverrUser.AccountUser +'Im sending you ₹'+amount+' Continue your shopping through DjangoPAY :)'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [obj.email]
                send_mail( subject, message, email_from, recipient_list )
                user = Account.objects.get(AccountUser=request.user.username)
                return render(request,'profile.html',{"balance":user.balance,"msg":msg})
            else:
                senderUser = Account.objects.get(AccountUser=request.user.username)
                receiverrUser =  Account.objects.get(AccountUser=username)
                obj=User.objects.get(username=receiverrUser)
                senderUser.save()
                receiverrUser.save()
                msg = "Transaction Success"
                subject = ' In Need of money '
                message = ' Hi '+receiverrUser.AccountUser +'Can you please credit me ₹ '+Requiredamount
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [obj.email]
                send_mail( subject, message, email_from, recipient_list )
                user = Account.objects.get(AccountUser=request.user.username)
                return render(request,'profile.html',{"balance":user.balance,"msg":msg})
        except Exception as e:
            msg = "Transaction Failure, Please check and try again"
    else:
        user = Account.objects.get(AccountUser=request.user.username)
        return render(request,'profile.html',{"balance":user.balance})
    


def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = Userform(request.POST)
        if user_form.is_valid():
           
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(user_form.errors)
    else:
        user_form = Userform()
    return render(request,'auth/signup.html',{'user_form':user_form,
                                            'registered':registered})

def viewall(request):
    return render(request,'viewall.html')

def login(request):    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')        
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request,user)
                return redirect('/load')
                return redirect('/proview')
            else:    
                return render(request, 'auth/check.html')
        else:
            return render(request, 'auth/check.html')
    else:
        return render(request, 'auth/login.html')
 

def Acc_view(request):
    msg=''
    form=''
    if request.method =='POST':
        form=CustomForms(request.POST)
        if form.is_valid():
            account=Account(
                AccountUser=form.cleaned_data.get('user'),
                typeaccount=form.cleaned_data.get('typeaccount'),
                balance=form.cleaned_data.get('balance'))
           
            account.save()
            msg='Your account created Successfully!!!'
            return render(request,'form.html',{"msg":msg,"forms":form})
            
        else:
            msg=form.errors

    else:
        form=CustomForms()
    return render(request,'form.html',{
        "msg":msg,
        "forms":form
     })

def Dummy(request):
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            q=form.cleaned_data.get('q')
            obj=Account.objects.filter(name__contains=q)
            form=None
            return render(request,'tempo.html',{'obj':obj,'form':form})
    else:
        form=SearchForm()
        b=Account.objects.all()
        return render(request,'tempo.html',{'obj':b,'form':form})

def logout(request):
    return redirect('/')

def sendmoney(request):
    return render(request,'sendmoney.html')

def email(request):

    username = request.POST["username"]
    amount = request.POST["amount"]
    senderUser = Account.objects.get(AccountUser=request.user.username)
    receiverrUser =  Account.objects.get(AccountUser=username)
    obj=User.objects.get(username=receiverrUser)

