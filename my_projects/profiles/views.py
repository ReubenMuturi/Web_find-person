from django.shortcuts import render, redirect
from .models import MissingPerson, MatchingPerson
from .forms import MissingPersonForm, MatchingPersonForm
from .models import Profile

# Home view for the root URL
def home(request):
    return render(request, 'home.html')  # Renders home.html template


def profile_list(request):
    profiles = Profile.objects.all()  # Assuming Profile is a model for general user profiles
    return render(request, 'profile_list.html')


def create_missing_profile(request):
    if request.method == 'POST':
        form = MissingPersonForm(request.POST, request.FILES)  # Handles file uploads
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, 'create_missing_profile.html')
    else:
        form = MissingPersonForm()  # If the form is not submitted, display an empty form
    return render(request, 'create_missing_profile.html', {'form': form})  # Render the form in the template

def create_matching_profile(request):
    if request.method == 'POST':
        form = MatchingPersonForm(request.POST, request.FILES)  # Handles file uploads
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, 'create_matching_profile.html')
    else:
        form = MatchingPersonForm()  # Display an empty form if not submitted
    return render(request, 'create_matching_profile.html', {'form': form})  # Render the form in the template

from django.shortcuts import render
from .models import MissingPerson, MatchingPerson

# View to list all missing persons
# View to list all missing persons
def missing_persons_list(request):
    missing_persons = MissingPerson.objects.all()  # Fetch all missing persons from the database
    return render(request, 'missing_persons_list.html', {'missing_persons': missing_persons})

# View to list all matching persons
def matching_persons_list(request):
    matching_persons = MatchingPerson.objects.all()  # Fetch all matching persons from the database
    return render(request, 'matching_persons_list.html', {'matching_persons': matching_persons})