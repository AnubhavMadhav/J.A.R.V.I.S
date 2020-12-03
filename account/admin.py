from django.contrib import admin
from account.models import Contact, Email, WhatsApp

# Register your models here.
admin.site.register(Contact)
admin.site.register(Email)
admin.site.register(WhatsApp)