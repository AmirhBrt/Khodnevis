from django.contrib import admin

from contents.models import Content, Rating


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Rating)
class ContentRatingAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
