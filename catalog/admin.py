from django.contrib import admin

from.models import Author
from.models import Book
from.models import BookInstance
from.models import Genre
from.models import Language

# Register your models here.
# @admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death', 'hobby', 'hometown')
    fields = [('first_name', 'last_name'), 'hobby', 'hometown', ('date_of_birth', 'date_of_death')]
    pass

class BookInstanceInline(admin.TabularInline):
    extra = 0
    model = BookInstance
    

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
    pass

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )
    pass


admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book, BookAdmin)
# admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
admin.site.register(Language)