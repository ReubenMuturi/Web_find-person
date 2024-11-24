# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# User Model
class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='profiles_user_set',  # New related_name to prevent conflict
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='profiles_user_permissions_set',  # New related_name to prevent conflict
        blank=True,
    )
# Missing Person Model
class MissingPerson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='missing_persons')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    description = models.TextField()
    last_seen_location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='missing_persons/', null=True, blank=True)

# Matching Person Model
class MatchingPerson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matching_persons')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    description = models.TextField()
    found_location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='matching_persons/', null=True, blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
