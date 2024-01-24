from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.messages import add_message

User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')

        error = "Неправильный логин или пароль!"
        return render(request, 'auth/login.html', locals())

    return render(request, 'auth/login.html', locals())


def signup_logics(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password != repassword:
            return render(request, 'users/sign_up.html', {'error': "Пароли не совпадают!"})

        if User.objects.filter(username=username).exists():
            return render(request, 'users/sign_up.html', {'error': "Такой пользователь уже есть!"})

        user = User.objects.create_user(
            username=username,
            password=password,
        )
        login(request, user)
        return redirect('homepage')

    return render(request, 'users/sign_up.html')