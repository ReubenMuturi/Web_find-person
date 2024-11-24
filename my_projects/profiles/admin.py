from .models import Profile
from django.contrib import admin
from .models import User, MissingPerson, MatchingPerson

admin.site.register(User)  # Register the User model
admin.site.register(MissingPerson)  # Register the MissingPerson model
admin.site.register(MatchingPerson)  # Register the MatchingPerson model

admin.site.register(Profile)
# Register your models here.
