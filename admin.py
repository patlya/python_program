
from django.contrib import admin
from .models import *
# Register your models here.
@admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

class ImegeData(admin.ModelAdmin):
    list_display = ('title','Image','description')
    list_editable = ('Image',)
    list_per_page = 2
    search_fields = ('title',)
    list_filter = ('title',)
    actions = [make_published]

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]    
class ItemInline(admin.StackedInline):
    model = CartItem
    extra = 2 

class CartAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ["created", "total_price", "paid"]

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'born_in_fifties')
    list_display_links = ('first_name',)

admin.site.register(Image,ImegeData)
admin.site.register(Author, AuthorAdmin,)
admin.site.register(Book)
admin.site.register(Cart, CartAdmin)
admin.site.register(Item)

admin.site.register(Person,PersonAdmin,)    