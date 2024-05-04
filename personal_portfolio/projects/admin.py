# projects/admin.py


from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')

    def has_add_permission(self, request):
        return False

admin.site.register(Project, ProjectAdmin)