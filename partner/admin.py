from django.contrib import admin
from . models import Partner


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym', 'email', 'phone', 'country', 'state', 'lga', 'website')
    # list_editable = ('name', 'email', 'phone')
    list_filter = ('date_created', 'date_updated')
    search_fields = ('name', 'email', 'phone')
    list_display_links = ('website',)

admin.site.register(Partner, PartnerAdmin)