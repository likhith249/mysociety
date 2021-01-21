from django.contrib import admin

# Register your models here.
from . models import Society,Member

admin.site.register(Society)
admin.site.register(Member)