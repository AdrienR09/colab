from rest_framework import serializers
from .models import Profile, Item, ITEM_TYPES
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):

    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name')
        user.last_name = self.validated_data.get('last_name')
        user.save(update_fields=['first_name', 'last_name'])

class ProfileSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner')

    class Meta:
        model = Profile
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner')

    class Meta:
        model = Item
        fields = '__all__'