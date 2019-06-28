from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomForms,Userform,SearchForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login,authenticate
from .models import Account

# Create your views here.
# def profile(request):
#     # form=''
    
#     # if request.method == 'GET':
#     #     form = CustomForms()
        
#     #     # user=Account.objects.get(AccountUser=AccountUser)
#     #     if form.is_valid():
#     #         form.save()
            
#     #         return render(request,'profile.html',{'form':form})
#     # instance = Account(AccountUser = request.AccountUser, balance = 0)
#     # instance.save()
#     user = Account.objects.get(AccountUser=request.user.username)
#     return render(request,'profile.html',{"balance":user.balance})

    # if form.is_valid():
def profile(request):
    user=''
    msg=""
    if request.method == "POST":
        try:
            username = request.POST["username"]
            amount = request.POST["amount"]
            senderUser = User.objects.get(username=request.user.username)
            receiverrUser =  User.objects.get(username=username)
            sender = balance.objects.get(user = senderUser)
            receiverr = balance.objects.get(user = receiverrUser)
            sender.balance = sender.balance - int(amount)
            receiverr.balance = receiverr.balance + int(amount)
            sender.save()
            receiverr.save()
            msg = "Transaction Success"

            user = Account.objects.get(AccountUser=request.user.username)
            return render(request,'profile.html',{"balance":user.balance})
        except Exception as e:
            print(e)
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
                return redirect('/proview')
            else:
                print("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
    else:
        return render(request, 'auth/login.html')

def check(request):
    return render(request,'check.html') 

def Acc_view(request):
    msg=''
    form=''
    # context=None
    if request.method =='POST':
        form=CustomForms(request.POST)
        if form.is_valid():
            account=Account(
                AccountUser=form.cleaned_data.get('user'),
                typeaccount=form.cleaned_data.get('typeaccount'),
                #genre=form.cleaned_data.get('genre'),
                balance=form.cleaned_data.get('balance'))
            # book=Book.objects.create(name=form.cleaned_data.get('name'),purchase_date=form.cleaned_data.get('purchase_date'),genre=form.cleaned_data.get('genre'),author=form.cleaned_data.get('author')) ......this can also be written instead of previous one
            account.save()
            msg='account created Successfully'
        else:
            
            msg=form.errors
    # context={
    #     "msg":msg,
    #     "forms":form
    #  }

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
            print('reeerethu')
            q=form.cleaned_data.get('q')
            obj=Account.objects.filter(name__contains=q)
            form=None
            return render(request,'tempo.html',{'obj':obj,'form':form})
    else:
        print('sdgdsfgsdfg')
        form=SearchForm()
        b=Account.objects.all()
        return render(request,'tempo.html',{'obj':b,'form':form})

def logout(request):
    return redirect('/')