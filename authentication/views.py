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

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [CustomPermissions]

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class ItemCreateOrList(generics.CreateAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [CustomPermissions]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user)

    def get(self, request, format=None):
        if "profile" in request.GET.keys():
            try:
                items = Item.objects.filter(profile=Profile.objects.get(pk=int(request.GET["profile"]))).all()
                serializer = ItemSerializer(items, many=True)
                return Response(serializer.data)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            items = Item.objects.all()
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data)