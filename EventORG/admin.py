from django.contrib import admin
from .models.Notificaton import Notification

class Noti_Admin(admin.ModelAdmin):
    list_display = ('eid', 'message', 'date', 'sent')
    list_editable = ('message', 'date', 'sent')

admin.site.register(Notification, Noti_Admin)