from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Myuser(AbstractUser):
    weixin=models.CharField(max_length=10,verbose_name = '微信号')
    phone=models.CharField(max_length=10,verbose_name = '联系电话')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['id']






class Category(models.Model):
    name = models.CharField(max_length = 10,verbose_name = '种类名字')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '种类'
        verbose_name_plural = '种类'
        ordering=['id']

class Tag(models.Model):
    name=models.CharField(max_length = 50,verbose_name ='标签名称',)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'



class Article(models.Model):
    title =  models.TextField(verbose_name = '文章标题')
    desc = models.CharField(max_length=50,verbose_name = '文章简介')
    content = models.TextField(verbose_name='文章内容')
    date_publish = models.DateField(auto_now_add=True,verbose_name = '提交时间')
    click_count = models.IntegerField(verbose_name = '点击次数')

    user = models.ForeignKey(Myuser,on_delete=models.CASCADE,verbose_name = '所属用户')
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name = '文章类型')
    tag = models.ManyToManyField(Tag,through='Article_Tag')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering=['-date_publish']


class Article_Tag(models.Model):
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)


class Comment(models.Model):
    username = models.CharField(max_length=12,verbose_name='评论的用户')
    content = models.TextField(verbose_name='评论内容')
    date_publish = models.DateField(auto_now_add = True,verbose_name='评论时间')
    article_comment = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name='评论的对象文章')
    parent_cmt = models.ForeignKey('Comment',on_delete=models.CASCADE,null=True,blank=True,verbose_name='父评论')

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'



