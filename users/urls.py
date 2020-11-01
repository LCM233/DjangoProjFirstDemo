"""users定义URL模式"""
# 在Django2.0中内置登陆视图不再是函数，而是类，位置在django.contrib.auth.views.LoginView,template_name是类的属性
from django.urls import path,re_path
# 导入默认视图login
from django.contrib.auth.views import LoginView
from . import views
"""
    鉴于我们没有编写自己的视图函数，我们传递了一个字典，
    告诉Django去哪里查找我们将编写的模板。
    这个模板包含在应用程序users 而不是learning_logs中。 
"""
urlpatterns = [
    # 登录页面
    path(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    path(r'^logout/$',views.logout_view,name='logout'),
    path(r'^register/$',views.register,name='register'),
]
app_name = 'users'