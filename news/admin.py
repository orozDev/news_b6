from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category, Tag


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'date', 'is_published', 'get_image')
    list_display_links = ('id', 'name')
    list_editable = ('is_published',)
    list_filter = ('category', 'tags', 'is_published', 'date')
    search_fields = ('name', 'author', 'description', 'content')
    readonly_fields = ('views', 'date', 'updated', 'get_full_image')

    @admin.display(description='Изображение')
    def get_full_image(self, news):
        return mark_safe(f'<img src={news.image.url if news.image else "-"} width="50%" />')

    @admin.display(description='Изображение')
    def get_image(self, news):
        return mark_safe(f'<img src={news.image.url if news.image else "-"} width="150px" />')


admin.site.register(Category)

admin.site.register(Tag)

# Register your models here.
