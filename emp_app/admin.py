from django.contrib import admin

from .models import Department,Role,Employee

admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)

# Register your models here.
