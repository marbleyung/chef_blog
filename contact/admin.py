from django.contrib import admin
from .models import *


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    list_display_links = ('name', )

    class Meta:
        models = ContactModel


admin.site.register(ContactModel, ContactModelAdmin)
admin.site.register(ContactLink)
admin.site.register(About)
admin.site.register(AboutImage)
admin.site.register(Social)
