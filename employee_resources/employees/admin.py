from django.contrib import admin

from .models import Employee, Position, Rank

admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Rank)
