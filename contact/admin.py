from django.contrib import admin
from contact.models import ContactModel

class ContactModelModelAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Message')

admin.site.register(ContactModel, ContactModelModelAdmin)