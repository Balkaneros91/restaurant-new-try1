from django.contrib import admin
from .models import Category, MenuItem
from django_summernote.admin import SummernoteModelAdmin


# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)


# admin.site.register(MenuItem)
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('name', 'category', 'description', 'price')
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name', 'category')
    summernote_fields = ('description')
