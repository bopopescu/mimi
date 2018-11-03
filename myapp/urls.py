from django.urls import path
from myapp.views import *

app_name='myapp'

urlpatterns = [
    path('first/',New_article,name='first'),
    path('category/<int:cid>',category,name='category'),
    path('acticle_page/',acticle_page,name='acticle_page'),
    path('article/',article,name='article'),
    path('reg/',reg,name='reg'),
    path('reg1/',reg1,name='reg1'),
    path('login/<aid>/',gologin,name='login'),
    path('login1/',login1,name='login1'),
    path('logout/',log_out,name='logout'),
    path('cmt1/<aid>/',cmt1,name='cmt1'),

]