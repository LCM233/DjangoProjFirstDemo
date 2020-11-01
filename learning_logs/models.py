from django.db import models
# 导入模型User
from django.contrib.auth.models import User

# django模型字段参考为https://docs.djangoproject.com/en/1.8/ref/models/fields/ 
# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length = 200) # 限制字符长度200
    date_added = models.DateTimeField(auto_now_add = True)
    # 建立到模型User的外键关系
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE) #外键,关联数据删除时删除关联
    text = models.TextField() # 不限制文字长度
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        """"
        用于管理模型的额外信息。
        在让Django在需要时使用Entries 来表示多个条目。
        如果没有这个类，Django将使用Entrys来表示多个条目。
        """
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        if len(self.text) > 50 :
            return self.text[:50] + "..."
        else:
            return self.text