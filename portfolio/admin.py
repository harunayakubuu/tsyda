from django.contrib import admin
from . models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'completed', 'date_completed')
    search_fields= ('project_title', 'about_project', 'categories')
    list_filter = ('date_completed', 'completed')

admin.site.register(Project, ProjectAdmin)