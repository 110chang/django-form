from django.contrib import admin
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'kana', 'email', )
    list_display_links = ('name', )

admin.site.register(Contact, ContactAdmin)
