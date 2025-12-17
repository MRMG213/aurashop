from django.shortcuts import render, redirect
from .models import User

def index(request):
    if 'username' in request.GET:
        name = request.GET['username']
        password = request.GET.get('password', '12345')
        User.objects.create(username=name, password=password)
    
    users = User.objects.all()
    
    return render(request, 'main/index.html', {'users': users})

def login_view(request):
    error_message = ""
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                return redirect('/')
            else:
                error_message = "Неверный пароль"
        except User.DoesNotExist:
            error_message = "Пользователь не найден"
    
    return render(request, 'main/login.html', {'error': error_message})

def register_view(request):
    success_message = ""
    error_message = ""
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        
        if password != password2:
            error_message = "Пароли не совпадают"
        elif User.objects.filter(username=username).exists():
            error_message = "Пользователь с таким логином уже существует"
        else:
            User.objects.create(
                username=username,
                password=password,
                first_name=first_name,
                email=email
            )
            success_message = "Регистрация успешна! Теперь вы можете войти."
    
    return render(request, 'main/register.html', {
        'success': success_message,
        'error': error_message
    })
def profile_view(request):
    return render(request, 'main/profile.html')
def cart_view(request):
    return render(request, 'main/cart.html')
def admin_view(request):
    return render(request, 'main/admin.html')