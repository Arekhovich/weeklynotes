from django.contrib import admin

from note.models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'text', 'author')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Note, NoteAdmin)
# Register your models here.
