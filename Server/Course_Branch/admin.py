from django.contrib import admin

# Register your models here.
from .models import COURSE,BRANCH

admin.site.register(COURSE)
admin.site.register(BRANCH)