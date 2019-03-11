from django.contrib import admin

# Register your models here.
from .models import POST, VOTES_STATUS

admin.site.register(POST)
admin.site.register(VOTES_STATUS)