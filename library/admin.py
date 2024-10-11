from django.contrib import admin

from library import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date")
    search_fields = ("first_name", "last_name")
    list_filter = ("birth_date",)


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_date")
    search_fields = ("title", "author__first_name", "author__last_name")
    list_filter = ("publication_date", "author")
    autocomplete_fields = ("author",)
