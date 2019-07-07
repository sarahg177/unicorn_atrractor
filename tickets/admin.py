from django.contrib import admin
from .models import Bug, Vote, Comments

# Register your models here.
admin.site.register(Bug)
admin.site.register(Vote)
admin.site.register(Comments)
