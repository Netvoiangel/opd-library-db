from django.contrib import admin
from .models import Author, PDFFile

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'position', 'institute')
    search_fields = ('last_name', 'first_name', 'middle_name', 'position', 'institute')

@admin.register(PDFFile)
class PDFFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'direction')
    search_fields = ('title', 'direction')
    filter_horizontal = ('authors',)
