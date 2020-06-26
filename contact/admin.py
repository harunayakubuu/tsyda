from django.contrib import admin

# Register your models here.
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'date_recieved', 'date_updated')
    list_filter  = ('date_recieved', 'date_recieved')
    search_fields = ('name', 'email', 'phone', 'message')
    list_per_page = 50
    list_display_links = ('email', )

admin.site.register(Contact, ContactAdmin)