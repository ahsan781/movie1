
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
import re
# Create your views here.
def login1(request):
    if request.method == "POST":
            # Get the post parameters
      
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  
        if user is not None:
            login(request, user)
            return redirect('/mainpage')

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return render(request, "signin.html")
    return render(request, 'signin.html' )
    

def signup(request):

     if request.method == "POST":
            # Get the post parameters
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        city = request.POST['city']
        ad1 = request.POST['ad1']
        ad2 = request.POST['ad2']
        pc = request.POST['pc']
        phone1 = request.POST['phone']
        country1 = request.POST['country']
        lu = request.POST['lu']
          


        checkemail = User.objects.filter(email=email)
        checkuser = User.objects.filter(username=username)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if len(checkemail)>0:
            messages.error(request, "Email is already exits.")
            return render(request, 'signup.html')
        if len(checkuser)>0:
            messages.error(request, "User Name is already exits.")
            return render(request, 'signup.html')

        if len(username) > 10:
            messages.error(request, " Your user name must be under 10 characters")
            return render(request, 'signup.html')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return render(request, 'signup.html')
        if password != cpassword:
            messages.error(request, " Passwords do not match")
            return render(request, 'signup.html')
        
        if(re.search(regex,email)):   
           print("Valid Email")   
        else:   
           messages.error(request, " invalid email")
           return render(request, 'signup.html') 
         
        # Create the user
        user = User.objects.create_user(username, email, password)
        address = Address(user = user , city = city , Address1 = ad1 , Address2 = ad2,  postalcode = pc , phone = phone1 , country = country1 , lastupdate = lu)
        address.save()
        user.save()
        
        messages.success(request, "You have succesfully Registerd.")
        return redirect('/')
     return render(request, 'signup.html')

def mainpage(request):
     
    mediacat= mediacatagory.objects.all()
    media1 = media.objects.all()
    context ={'mediacat' : mediacat , 'media' : media1}
    return render(request, 'mianpage.html' , context)


def mediapage(request , id):
     
    mediacat= mediacatagory.objects.all()
    mediacat1 = mediacatagory.objects.filter(id = id)
    media1 = media.objects.all()
    medialist = media.objects.filter( mediacatagory1 = id)
    context ={'mediacat' : mediacat , 'media' : media1 , 'mediacat1':mediacat1 , 'medialist': medialist }
    return render(request, 'media.html' , context)

def loanpage(request , id):
     
    mediacat= mediacatagory.objects.all()
     
    media1 = media.objects.all()
    context ={'mediacat' : mediacat , 'media' : media1  }
    if request.method == "POST":
            # Get the post parameters
        media1 = media.objects.filter(id = id)
        print(media1)
        media2 = media.objects.get(id = id)
        print(media2)
        ld = request.POST['ld']
        rd = request.POST['rd']
        user1 = User.objects.get(username=request.user.username) 
        addloan = loan(userid = user1 , mediaid = media2 , loandate = ld ,returndate= rd )
        media2.media_status = True
        media2.save()
        addloan.save()
        return redirect('/mainpage')

        
    return render(request, 'loan.html' , context )
def ulogout(request):
    logout(request)
    return redirect('/')

def profile(request , id):
    mediacat= mediacatagory.objects.all()
    media1 = media.objects.all()
    user1 = User.objects.get(pk=id)
    address1 = Address.objects.filter(user = id)
    context ={'mediacat' : mediacat , 'media' : media1, 'user1' : user1 , 'address1': address1}
    if request.method == "POST":
            # Get the post parameters
      
        username = request.POST['name']
        city = request.POST['city']
        ad1 = request.POST['ad1']
        ad2 = request.POST['ad2']
        pc = request.POST['pc']
        phone = request.POST['phone']
        country = request.POST['country']
        reg = User.objects.get(pk=id)
        reg1  = Address.objects.get(user = id)
        reg.username = username
        reg1.city = city
        reg1.Address1 = ad1
        reg1.Address2 = ad2
        reg1.postalcode  = pc
        reg1.phone  = phone
        reg1.country = country
        reg1.save()
        reg.save()
        return redirect('/mainpage')
    return render(request, 'Profile.html' , context)