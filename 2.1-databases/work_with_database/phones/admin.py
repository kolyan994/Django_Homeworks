from django.contrib import admin

from .models import Phone

@admin.register(Phone)
class Phone_admin(admin.ModelAdmin):
	pass
