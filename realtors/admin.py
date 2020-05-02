from django.contrib import admin

# Register your models here.

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ['id','Name','email','hire_date','is_mvp']
    list_display_links = ['id','Name']
    list_editable =['is_mvp',]
    list_per_page = 25
    search_fields =['Name',]


admin.site.register(Realtor,RealtorAdmin)
