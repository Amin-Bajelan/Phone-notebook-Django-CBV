from django.contrib import admin
from phone_number.models import Contact


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name_contact', 'phone_number')
    list_filter = ('owner', 'name_contact', 'phone_number')


admin.site.register(Contact, ContactAdmin)
