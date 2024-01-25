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


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'auth/profile.html'
    pk_url_kwarg = 'pk'


def change_avatar(request, pk):
    if request.method == 'POST':
        user = User.objects.get(id=pk)

        avatar = request.FILES.get('avatar')
        user.avatar = avatar
        user.save()

        return redirect('profile', user.id)
