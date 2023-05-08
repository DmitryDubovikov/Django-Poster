from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Place, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ["image_preview"]
    ordering = [
        "order",
    ]

    def image_preview(self, obj):
        return format_html(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=200,
                height=200,
            )
        )


class ImageInline(admin.TabularInline):
    model = Image

    readonly_fields = ["image_preview"]
    ordering = [
        "order",
    ]

    def image_preview(self, obj):
        return format_html(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=200,
                height=200,
            )
        )


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlaceAdmin)
