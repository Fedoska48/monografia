from django.contrib import admin

from .models import Book, Comment, Category


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
        'book_year',
        'book_author',
        'book_publisher',
        'book_image',
        'book_file',
        'category',
    )
    list_editable = ('category',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "description", 'books')
    search_fields = ("title",)
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'author',
        'book',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Comment, CommentAdmin)
