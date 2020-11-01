from django.shortcuts import render, get_object_or_404
from .models import Topic,Entry
from django.http import HttpResponseRedirect,Http404, HttpResponse
from django.urls import reverse
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
# @login_required装饰器，检查用户是否登录
# Create your views here.
""""
render作用:
    URL请求与我们刚才定义的模式匹配时，
    Django将在文件views.py中查找函数index() ，
    再将请求对象传递给这个视图函数。
"""
def index(request):
    """学习笔记的主页"""
    # render两个参数为原始请求对象和一个可用于创建网页的模板
    return render(request,'learning_logs/index.html')

# 仅当用户已登录才显示topics页面，需要修改settings
@login_required
def topics(request):
    """显示所有主题"""
    # render第三个参数为字典数据
    topics = Topic.objects.filter(owner = request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    """显示单个主题中的所有条目"""
    topic = get_object_or_404(Topic,id=topic_id)
    if topic.owner != request.user:
        raise Http404
    # 拿到外键关联内容，减号表示倒序
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    # 用户初次请求的是空表单（GET请求）返回一个空表单
    if request.method != 'POST':
        form = TopicForm()
    else:
        # post提交的数据存在request.POST中，对数据处理
        form = TopicForm(request.POST)
        # is_valid()方法判断用户填了所有必不可少的字段
        if form.is_valid(): 
            # request对象获取当前用户
            # 确认用户后,将表单内容写入数据库
            new_topic = form.save(commit = False)
            new_topic.owner = request.user
            new_topic.save()
            # 返回原页面，reverse()将URL模型转换为URL，传给HttpResponseRedirect()重新定向到页面
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    # 单个主题
    topic = get_object_or_404(Topic,id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST)
        if form.is_valid():
            # 让Django新建一个条目对象，存入new_entry，但不存入数据库
            new_entry = form.save(commit = False)
            new_entry.topic = topic # 获得正确的主题
            new_entry.save() # 存入数据库
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry = get_object_or_404(Entry,id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # 创建一个EntryForm实例并用既有条目填充他：instance的作用
        form = EntryForm(instance = entry)
    else:
        # 用户填写完数据提交
        form = EntryForm(instance = entry,data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)

@login_required 
def del_entry(request,entry_id):
    """删除现有条目"""
    pass

def del_topic(request,topic_id):
    """删除现有主题"""
    pass