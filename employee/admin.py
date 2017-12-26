# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from employee.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department')
    search_fields = ['id', 'name', 'department']
    list_filter = ['department']

admin.site.register(Employee, EmployeeAdmin)