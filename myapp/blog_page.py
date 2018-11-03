from django.core.paginator import PageNotAnInteger,Paginator


def getblog_bypage(request,article_list):
    try:
        page_number=int(request.GET.get('page',1)) #当前为page_number页
        paginator=Paginator(article_list,2)  #将文章总集合article_list按照每页2条显示
        page=paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)

    return page



