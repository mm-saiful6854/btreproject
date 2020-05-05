from django.contrib import admin

# Register your models here.

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','listing','contact_date','user_id']
    list_display_links = ['id','name']
    search_fields = ['name','email','listing','contact_date']
    list_per_page =25


admin.site.register(Contact,ContactAdmin)
