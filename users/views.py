from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout,authenticate,login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        # UserCreationForm函数处理的是:
            # 用户名未包含非法字符，
            # 输入的两个密码相同，
            # 以及用户没有试图做恶意的事情
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # 将账号和密码散列值保存到数据库
            new_user = form.save()
            # authenticate方法返回一个通过身份验证的用户对象
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            # 函数login为新用户创建有效的对话
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form':form}
    return render(request, 'users/register.html', context)
