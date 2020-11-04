from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')


def handleBlog(request):
    if not request.user.is_authenticated:
        messages.info(request,"Please login and try again")
        return redirect('/login')


    return render(request,'handleBlog.html')


def services(request):
    return render(request,'services.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'signup.html')
            
            
        try:
            if User.objects.get(username=username):


                messages.warning(request,"UserName is Taken")
                return render(request,'signup.html')

        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return render(request,'signup.html')

        except Exception as identifier:
            pass
        
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        messages.info(request,"Signup SuccessFull! Please Login ")
        return redirect('/login')

    return render(request,'signup.html')



def handlelogin(request):
    if request.method=="POST":

        username=request.POST['username']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return render(request,'index.html')

        else:
            messages.error(request,"Something went wrong")
            return redirect('/login')

    return render(request,'login.html')    



def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect('/login')
        

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        numb=request.POST.get('num')
        desc=request.POST.get('desc')
        # print(name,email,numb,desc)
        query=Contact(name=name,email=email,phone_number=numb,description=desc)
        query.save()
        messages.info(request,'Thanks For Contacting US! will get back you soon')
        return redirect('/contact')



    return render(request,'contact.html')        