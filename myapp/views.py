from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from myapp.blog_page import getblog_bypage
from myapp.models import *



def New_article(request):
    article_list = Article.objects.all()
    page = getblog_bypage(request, article_list)
    return render(request,'index.html',locals())

def  category(request,cid):    #文章种类表选择
    article_list = Article.objects.filter(category_name_id=cid)    #根据models中Article的多对一关联关系，选择这个种类的所有文章
    page = getblog_bypage(request,article_list)
    return render(request,'index.html',locals())

def acticle_page(request):      #分页
    cid = request.GET.get("cid")
    if cid:
        article_list = Article.objects.filter(category_name_id=cid)
        page = getblog_bypage(request,article_list)
        return  render(request,'index.html',locals())
    else:
        article_list=Article.objects.all()
        page = getblog_bypage(request,article_list)
        return render(request,'index.html',locals())


def article(request):  #根据标题查看文章
    aid = request.GET.get('aid')
    article=Article.objects.get(id=aid)
    comment_list = article.comment_set.all()
    return render(request,'article.html',locals())

def reg(request):  #进入注册界面
    return render(request,'reg.html')


def reg1(request):  #注册用户信息
        regname = request.POST.get('regname')
        regeamil = request.POST.get('regemil')
        regphone = request.POST.get('regphone')
        regpwd = request.POST.get('regpwd')
        Myuser.objects.create_user(username=regname,email=regeamil,phone=regphone,password=regpwd)
        return HttpResponseRedirect('/myapp/login/')

def gologin(request):  #进入登录界面
    return render(request,'login.html')
def login1(request,aid): #登录
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username,password=password)
    if user:
        login(request,user)
        return HttpResponseRedirect('/myapp/article/?aid/')
    else:
        return render(request,'login.html')

def log_out(request):   # 注销
    logout(request)
    return render (request,'index.html')

def cmt1(request,aid):  #根据标题查看文章进行评论
    content = request.POST.get('cmtname')
    name = request.POST.get('name')
    Comment.objects.create(username=name,content=content,article_comment_id=aid)
    return HttpResponseRedirect('/myapp/article/?aid='+aid)




