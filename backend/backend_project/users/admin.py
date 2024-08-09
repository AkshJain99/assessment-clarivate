from django.contrib import admin
from accounts.models import Users, Settings

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'Email')

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('IsNotificationEnabled', 'IsNewDashboardEnabled', 'Timezone')
