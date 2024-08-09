from rest_framework import serializers
from .models import Users, Settings

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['FirstName', 'LastName', 'Email']

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['IsNotificationEnabled', 'IsNewDashboardEnabled', 'Timezone']
