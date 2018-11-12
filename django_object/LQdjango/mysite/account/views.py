from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():#判断输入的值是否有效
            cd = login_form.cleaned_data
            #使用authenticate函数来验证此用户是否是本网站用户，如果是，返回一个实例对象给user，否则返回None
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse('Wellcome You. You have been authenticated successfully')
            else:
                return HttpResponse('Sorry. Your username or password is not right.')
        else:
            return HttpResponse('Invalid login')

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, "account/login.html", {'form':login_form})

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)#这个参数让数据没有写入数据库
            new_user.set_password(user_form.cleaned_data['password2'])#将校验过的数据设置给对象
            new_user.save()
            return HttpResponse('successfully')
        else:
            return HttpResponse('sorry,your can not register.')
    else:
        user_form = RegistrationForm()
        return render(request, 'account/register.html', {'form':user_form})