from django.contrib import admin

from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name","middle_name","date_of_graduation","date_of_employment","position","salary","supervisors","employee_code")
    search_fields = ("first_name","middle_name")
admin.site.register(Employee,EmployeeAdmin)
