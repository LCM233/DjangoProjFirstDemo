"""定义learning_logs的URL模式"""
from django.urls import path
from django.urls import re_path
from . import views # 其中的句点让Python从当前的urls.py模块所在的文件夹中导入视图

urlpatterns = [
    # 主页
    path('',views.index,name='index'),
    # 显示所有的主题
    path('topics/',views.topics,name='topics'),
    # 主题的全部内容
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 用于添加新主题的网页
    path('new_topic',views.new_topic,name='new_topic'),
    # 用于添加新条目
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 用于编辑条目
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),
    # 用于删除
    
]
app_name ='learning_logs'
"""
/(?P<topic_id>\d+)/ 表示两个斜杆内的整数存topic_id实参内：
    * 括号是匹配URL中的值
    * ?P<topic_id> 将匹配值传入topic_id
    * \d+ 匹配斜杆内任何数字，无论多少位
"""
