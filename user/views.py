from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('Login Başarili!')
            return redirect('/')
        else:
            print('Kullanici Adi Veya Parola Hatali')
            return redirect('login')
    else:
        return render(request,'pages/User/login.html')

def register(request):
    
    if(request.method == 'POST'):
        # get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            #Username
            if User.objects.filter(username = username).exists():
                print('Bu kullanıcı Adı Daha Önce Kullanılmış')
                return redirect('register')
            else:
                #Email
                if User.objects.filter(email = email).exists():
                    print('Bu Email Adresi Daha Önce Kullanılmış')
                    return redirect('register')
                else:
                    #everything's allright
                    user = User.objects.create_user(username=username,password=password,email=email)
                    user.save()
                    print('Kullanıcı Oluşturuldu!')
                    return redirect('login')
        else:
            print('Parolalar Eşleşmiyor!')
            return redirect('register')

        return redirect('register')
    else:
        return render(request,'pages/User/register.html')

    

def logout(request):

    if request.method == 'POST':
        auth.logout(request)

    return redirect('/')
    