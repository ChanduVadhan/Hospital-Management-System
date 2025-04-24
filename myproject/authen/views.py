from django.shortcuts import render


from django.shortcuts import render,redirect


from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required


# Create your views here.


def login_(request):

    if request.method =="POST":
        username_data = request.POST['username']
        password_data = request.POST['password']

    try:
        user=User.objects.get(username=username_data)
        print(user.password,type(user.password))
        print(password_data,type(password_data))
        if password_data==user.password:
            login(request,user)
            if request.user.is_authenticated:
                return redirect('home')
    except:
        wrong=True
        return render(request,'login_.html',{'wrong':wrong})
    

def register(request):

    if request.method=="POST":

        firstname=request.POST['FirstName']
        lastname=request.POST['LastName']
        email=request.POST['Email']
        username=request.POST['username']
        password=request.POST['password']

    
        try:
            username_existed=User.objects.get(username=username)
            return render(request,'register.html',{'username_existed':username_existed})
        except:
            u=User.objects.create(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
            return redirect('login_')

    return render(request,'register.html')

login_required(login_url='login_')
def logout_(request):
    logout(request)

    return redirect('login_')


@login_required(login_url='login_')
def update_profile(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('profile')

    return render(request, 'update_profile.html')



    return render(request, 'change_password.html')
@login_required(login_url='login_')
def changepassword(request):

    if request.method=='POST':
        np=request.POST['password']
        user=User.objects.get(username=request.user)
        user.set_password(np)
        user.save()
        return redirect('login_')

    return render(request,'change_password.html')


@login_required(login_url='login_') 
def profile(request):
    
    return render(request,'profile.html')