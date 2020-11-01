from django import forms
from .models import Topic,Entry
# TopicForm继承了forms.ModelForm类
# 最简单的ModelForm 版本只包含一个内嵌的Meta类，
# 它告诉Django根据哪个模型创建表单
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        # 只包含字段[text]
        fields = ['text']
        # 字段text没有标签
        labels = {'text':''} 
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        # 只包含字段text
        fields = ['text']
        # 字段text没有标签
        labels = {'text':''}
        # 属性widgets是一个表单元素，设置为宽度80的文本区域，默认40
        widgets = {'text':forms.Textarea(attrs={'cols':80})}