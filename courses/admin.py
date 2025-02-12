

from django.contrib import admin
from .models import Course, Enrollment

@admin.register(Course)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price']


# Register your models here.
@admin.register(Enrollment)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ['user', 'course']

