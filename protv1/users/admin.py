from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Application, Certificate, CustomUser, TimeSlot

admin.site.register(CustomUser, UserAdmin)

admin.site.register(Certificate)
admin.site.register(TimeSlot)
admin.site.register(Application)