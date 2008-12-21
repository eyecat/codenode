from django.contrib import admin

from apps.bookshelf.models import Folder

class FolderAdmin(admin.ModelAdmin):
    #list_display = ('__unicode__', )
    search_fields = ('owner__username', 'owner__first_name', 'owner__last_name')


admin.site.register(Folder, FolderAdmin)

