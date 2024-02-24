from rest_framework import serializers
from .models import Profile, Item, ITEM_TYPES

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