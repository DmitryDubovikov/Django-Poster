from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from .models import Place, Image


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ["image_preview"]
    ordering = [
        "order",
    ]

    def image_preview(self, obj):
        return format_html(
            '<img src="{url}" width="{width}" height={height} />'.format_html(
                url=obj.image.url,
                width=200,
                height=200,
            )
        )


class ImageInline(SortableAdminMixin, admin.TabularInline):
    model = Image

    readonly_fields = ["image_preview"]
    ordering = [
        "order",
    ]

    def image_preview(self, obj):
        return format_html(
            '<img src="{url}" width="{width}" height={height} />'.format_html(
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
