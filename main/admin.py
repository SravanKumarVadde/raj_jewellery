from django.contrib import admin
from django.utils.html import format_html

from . import models

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_tag', 'slug', 'date_added')
    list_filter = ('category',)
    search_fields = ('name',)
    readonly_fields = ('thumbnail',)
    prepopulated_fields = {"slug": ('name',)}
    autocomplete_fields = ('category',)

    def thumbnail_tag(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="%s"/>' % obj.thumbnail.url
            )
        return "-"
    thumbnail_tag.short_description = "Thumbnail"


admin.site.register(models.Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(models.Category, CategoryAdmin)


class CatalogPdfAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(models.CatalogPdf, CatalogPdfAdmin)


admin.site.register(models.Rates)
