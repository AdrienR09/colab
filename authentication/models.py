from django.db import models
from django.contrib.auth.models import AbstractUser

ITEM_TYPES = [('technical', 'Technical'),
              ('theory', 'Theory'),
              ('scientific advice', 'Scientific Advice')]

class Profile(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    bio = models.TextField(blank=True)
    title = models.CharField(max_length=4, blank=True)
    position = models.CharField(max_length=10, blank=True)
    institution = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    orcid_number = models.CharField(max_length=20, blank=True)
    researchgate_link = models.URLField(blank=True)
    googlescholar_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)

    @property
    def owner(self):
        return self

    def __str__(self):
        return self.username

class Item(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    type = models.CharField(max_length=20, choices=ITEM_TYPES, blank=True)

    @property
    def owner(self):
        return self.profile

    def __str__(self):
        return self.title
