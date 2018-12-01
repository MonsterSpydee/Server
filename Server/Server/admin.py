gfrom django.contrib import admin
from Points.models import POINTS
from Post.models import POST, VOTES_STATUS
from Course_Branch.models import BRANCH, COURSE
from .models import User

admin.site.register(POINTS)
admin.site.register(POST)
admin.site.register(VOTES_STATUS)
admin.site.register(BRANCH)
admin.site.register(COURSE)
admin.site.register(User)