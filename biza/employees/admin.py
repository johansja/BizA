from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Employee

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'hq', 'store']
    list_filter = ['hq',]

admin.site.register(Employee, EmployeeAdmin)
