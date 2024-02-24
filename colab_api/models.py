from django.db import models
from django.contrib.auth.models import AbstractUser

ITEM_TYPES = [('technical', 'Technical'),
              ('theory', 'Theory'),
              ('scientific advice', 'Scientific Advice')]

class Profile(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=4, blank=True, null=True)
    position = models.CharField(max_length=10, blank=True, null=True)
    institution = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    orcid_number = models.CharField(max_length=20, blank=True, null=True)
    researchgate_link = models.URLField(blank=True, null=True)
    googlescholar_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    @property
    def owner(self):
        return self

    def __str__(self):
        return self.username

class Item(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    type = models.CharField(max_length=20, choices=ITEM_TYPES, blank=False)

    @property
    def owner(self):
        return self.profile

    def __str__(self):
        return self.title
