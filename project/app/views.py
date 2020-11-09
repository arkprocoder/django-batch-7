from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Contact,Blogs
# email import
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage
# Create your views here.
def index(request):
    return render(request,'index.html')


def handleBlog(request):
    if not request.user.is_authenticated:
        messages.info(request,"Please login and try again")
        return redirect('/login')
    posts=Blogs.objects.all()
    context={'posts':posts}
    return render(request,'handleBlog.html',context)


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
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphone=request.POST.get('num')
        fdesc=request.POST.get('desc')
        # print(name,email,numb,desc)
        query=Contact(name=fname,email=femail,phone_number=fphone,description=fdesc)
        query.save()
        from_email=settings.EMAIL_HOST_USER
        # Email starts here
        connection=mail.get_connection()
        connection.open()
        email_messge=mail.EmailMessage(f'Email from {fname}',f'Query : {fdesc}\nUser Email : {femail}\nPhone Number : {fphone}',from_email,['aneesurrehman423@gmail.com','belleringunner@gmail.com'],connection=connection)  
        email_client=mail.EmailMessage('ARK BLog',f'Hello {fname}\nGreetings of the day\n\nThanks For Visiting Our Blog will get back you soon',from_email,[femail],connection=connection)
        connection.send_messages([email_messge,email_client])
        connection.close()
        messages.success(request,"Thanks for Contacting Us")
         # https://myaccount.google.com/lesssecureapps
      
        return redirect('/contact')

    return render(request,'contact.html')        


def search(request):
    query=request.GET['search']
    if len(query)>78:
        allPosts=Blogs.objects.none()
    else:
        allPostsTitle=Blogs.objects.filter(title__icontains=query)
        allPostsContent=Blogs.objects.filter(description__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)

    if allPosts.count()== 0:
        messages.warning(request,"No Search Results")

    params={'allPosts':allPosts,'query':query}   
     
    return render(request,'search.html',params)