from django.contrib import admin
from myapp.models import *
# Register your models here.

admin.site.register([Myuser,Article,Category,Tag,Article_Tag,Comment])
