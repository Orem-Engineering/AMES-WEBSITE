from django.contrib import admin
from blogsapp.models import Blogs
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields =['notice_heading','notice_content']
admin.site.register(Blogs)