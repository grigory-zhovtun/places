from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px;">',
                obj.image.url
            )
        return '-'

    get_preview.short_description = 'Preview'

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
