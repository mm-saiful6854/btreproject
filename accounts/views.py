from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

from contacts.models import Contact

# Create your views here.


def login(request):

    if(request.method == 'POST'):

        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if(user is not None):
            auth.login(request,user)
            messages.success(request,"successfully logged in")
            return redirect('dashboard')
        else:
            messages.error(request,"invaild credential")
            return redirect('login')  

    return render(request, 'accounts/login.html')


def register(request):
    if(request.method=='POST'):
        # get form values 
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username  = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        con_pass= request.POST['password2']

        if(password == con_pass):
            if(User.objects.filter(username=username).exists()):
                messages.error(request,'Username was taken')
                return redirect('register')
            else:
                if(User.objects.filter(email=email).exists()):
                    messages.error(request,'Email address was taken')
                    return redirect("register")
                else:
                    user = User.objects.create_user(username=username,password=password,email=email,last_name= lastname,first_name=firstname)
                    user.save()
                    #messages.set_level(request, messages.SUCCESS)
                    messages.success(request,'Successfully register, you can log in')
                    return redirect('login')

        else:
            messages.error(request,"Password doesn't match")
            return redirect('register')

    return render(request, 'accounts/register.html')


def logout(request):
    if(request.method =='POST'):
        auth.logout(request)
        #messages.set_level(request, messages.SUCCESS)
        messages.success(request,'You are logged out')
        return redirect('index')
    


def dashboard(request):
    list_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context ={
        'contacts': list_contact,
    }

    return render(request, 'accounts/dashboard.html',context)
