from django.contrib import admin

from .models import Client, License


class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'poc_contact_name', 'poc_contact_email', 'admin_poc']


class LicenseAdmin(admin.ModelAdmin):
    list_display = ['client', 'package', 'license_type', 'created_datetime', 'expiration_datetime']

admin.site.register(Client, ClientAdmin)
admin.site.register(License, LicenseAdmin)