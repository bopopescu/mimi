from myapp.models import *
from blogs import settings

def global_settings(request):
    Blog_name=settings.Blog_name
    Blog_desc=settings.Blog_desc
    category_list=Category.objects.all()
    return locals()