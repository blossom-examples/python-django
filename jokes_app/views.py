from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Joke
from .forms import JokeForm

def home(request):
    """Home page view with a random joke."""
    joke = Joke.random()
    return render(request, 'jokes_app/home.html', {'joke': joke})

def joke_list(request):
    """List all jokes."""
    jokes = Joke.objects.all().order_by('-created_at')
    return render(request, 'jokes_app/joke_list.html', {'jokes': jokes})

def joke_detail(request, pk):
    """Show a single joke."""
    joke = get_object_or_404(Joke, pk=pk)
    return render(request, 'jokes_app/joke_detail.html', {'joke': joke})

def joke_create(request):
    """Create a new joke."""
    if request.method == 'POST':
        form = JokeForm(request.POST)
        if form.is_valid():
            joke = form.save()
            messages.success(request, 'Joke was successfully created.')
            return redirect('joke_list')
    else:
        form = JokeForm()
    return render(request, 'jokes_app/joke_form.html', {'form': form, 'action': 'Create'})

def joke_update(request, pk):
    """Update an existing joke."""
    joke = get_object_or_404(Joke, pk=pk)
    if request.method == 'POST':
        form = JokeForm(request.POST, instance=joke)
        if form.is_valid():
            joke = form.save()
            messages.success(request, 'Joke was successfully updated.')
            return redirect('joke_list')
    else:
        form = JokeForm(instance=joke)
    return render(request, 'jokes_app/joke_form.html', {'form': form, 'action': 'Update'})

def joke_delete(request, pk):
    """Delete a joke."""
    joke = get_object_or_404(Joke, pk=pk)
    if request.method == 'POST':
        joke.delete()
        messages.success(request, 'Joke was successfully deleted.')
        return redirect('joke_list')
    return render(request, 'jokes_app/joke_confirm_delete.html', {'joke': joke})

def random_joke(request):
    """Show a random joke."""
    joke = Joke.random()
    return render(request, 'jokes_app/joke_detail.html', {'joke': joke})