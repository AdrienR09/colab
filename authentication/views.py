from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status

from .models import Profile, Item
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, ItemSerializer
from .permissions import CustomPermissions

def email_confirm_redirect(request, key):
    return HttpResponseRedirect(
        f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"
    )

def password_reset_confirm_redirect(request, uidb64, token):
    return HttpResponseRedirect(
        f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
    )

class ProfileList(generics.ListAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [CustomPermissions]

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [CustomPermissions]

class ProfileItemList(APIView):

    def get(self, request, pk, format=None):
        items = Item.objects.filter(profile=Profile.objects.get(pk=pk)).all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class ItemList(generics.ListAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [CustomPermissions]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.list(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [CustomPermissions]

class ItemCreate(generics.CreateAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [CustomPermissions]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user)