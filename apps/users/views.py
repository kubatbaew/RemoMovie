from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout, get_user_model
from django.views import generic

User = get_user_model()


def logout_logics(request):
    logout(request)
    return redirect('login')


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
            return render(request, 'auth/sign_up.html', {'error': "Пароли не совпадают!"})

        if User.objects.filter(username=username).exists():
            return render(request, 'auth/sign_up.html', {'error': "Такой пользователь уже есть!"})

        user = User.objects.create_user(
            username=username,
            password=password,
        )
        login(request, user)
        return redirect('homepage')

    return render(request, '')


def profile(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'auth/profile.html', locals())


def change_avatar(request, pk):
    if request.method == 'POST':
        user = User.objects.get(id=pk)

        avatar = request.FILES.get('avatar')
        user.avatar = avatar
        user.save()

        return redirect('profile', user.id)


def change_profile(request, pk):
    if request.method == "POST":
        user = User.objects.get(id=pk)

        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return redirect('profile')

    return redirect('/')


def change_password(request, pk):
    if request.method == 'POST':
        user = User.objects.get(id=pk)

        old_password = request.POST.get('old_password')
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')

        if password != new_password:
            error = "Пароли не совпадают!"
            return render(request, 'auth/profile.html', locals())

        if not user.check_password(old_password):
            error = "Старый пароль не правильно"
            return render(request, 'auth/profile.html', locals())

        user.set_password(new_password)
        user.save()
        return redirect('profile', )

    return redirect('/')


def favorite_movie(request):
    user = request.user
    return render(request, 'auth/userfavoritelist.html', locals())
