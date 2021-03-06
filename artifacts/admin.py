from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from . import models


class ArtifactImageInline(admin.TabularInline):
    model = models.ArtifactImage
    extra = 1


class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('uploaded_at', 'item_no', 'name_he', 'status', 'is_private', 'is_featured')
    list_display_links = ('uploaded_at', 'item_no', 'name_he', 'status', 'is_private', 'is_featured')
    inlines = [
        ArtifactImageInline,
    ]


class PageBannerAdmin(admin.ModelAdmin):
    list_display = ('page', 'main_text_he', 'main_text_en', 'credit_he', 'credit_en', 'active')
    list_display_links = ('page', 'main_text_he', 'main_text_en', 'credit_he', 'credit_en', 'active')


class ArtifactImageCropAdmin(admin.ModelAdmin):
    list_display = ('image', 'small_thumbnail', 'small_thumbnail_vertical', 'big_thumbnail', 'cover', 'footer')
    list_display_links = ('image', 'small_thumbnail', 'small_thumbnail_vertical', 'big_thumbnail', 'cover', 'footer')


class ArtifactMaterialAdmin(admin.ModelAdmin):
    list_display = ('title_he', 'title_en')
    list_display_links = ('title_he', 'title_en')


class ArtifactTypeAdmin(admin.ModelAdmin):
    list_display = ('title_he', 'title_en')
    list_display_links = ('title_he', 'title_en')


class OriginAreaAdmin(admin.ModelAdmin):
    list_display = ('title_he', 'title_en', 'countries_list')
    list_display_links = ('title_he', 'title_en', 'countries_list')

    def countries_list(self, obj):
        return ",".join([x.name for x in obj.countries])

    countries_list.short_description = _('Countries')


admin.site.register(models.Artifact, ArtifactAdmin)
admin.site.register(models.ArtifactType, ArtifactTypeAdmin)
admin.site.register(models.ArtifactMaterial, ArtifactMaterialAdmin)
admin.site.register(models.PageBanner, PageBannerAdmin)
admin.site.register(models.OriginArea, OriginAreaAdmin)
