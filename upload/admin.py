from django.contrib import admin
from .models import  Item
# Register your models here.
#video
from embed_video.admin import AdminVideoMixin
#from django.contrib.auth.admin import UserAdmin
admin.site.register(Item)