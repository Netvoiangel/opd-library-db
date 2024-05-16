from django.contrib import admin

# Register your models here.

from libraryDataBase.models import Author, Article, MainTable

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(MainTable)