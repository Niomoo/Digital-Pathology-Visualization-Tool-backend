from django.contrib import admin
from .models import User, Project, Image, Judgement
# Register your models here.

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Judgement)
