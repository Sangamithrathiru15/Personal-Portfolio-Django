from django.contrib import admin

# Register your models here.
#to add the jobmodel to our admin site
from .models import Jobs
admin.site.register(Jobs)