from django.contrib import admin

# Register your models here.

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','listing','contact_date']
    list_diplay_links = ['id','name']
    list_search_fields = ['name','email']
    list_per_page =25


admin.site.register(Contact,ContactAdmin)
