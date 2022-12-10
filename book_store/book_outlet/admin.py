from django.contrib import admin
from .models import Book, Author, Address, Country

# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")


class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "postal_code", "city")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "address")


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "rating", "author",)
    list_display = ("title", "author",)


admin.site.register(Country, CountryAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
