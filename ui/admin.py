from django.contrib import admin
from django.utils.html import format_html

from ui.models import Pictogram


class PictogramAdmin(admin.ModelAdmin):
    class Media:
        css = {'all': ('css/admin.css',)}

    fields = ('text', 'audio', 'image')
    list_display = ('__str__', 'image_tag')
    list_display_links = ('__str__', 'image_tag')
    ordering = ('text',)
    search_fields = ['text']

    def image_tag(self, pictogram):
        return format_html(f'<img src="{pictogram.image.url}"/>')
    image_tag.short_description = 'Image'

admin.site.register(Pictogram, PictogramAdmin)
