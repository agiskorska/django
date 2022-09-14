from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Animal

def home(request):
    data = { "animals" : Animal.objects.all()}
    return render(request, 'home.html', data)

def about(request):
    return HttpResponse("<h1>About</h1><p>We stock animals that shouldn't exist</p>")

def show(request, id):
    animal = get_object_or_404(Animal, pk=id)

    return render(request, 'animal.html', { "animal": animal })

def not_found_404(request, exception):
    data = { "error" : exception }
    return render(request, "404.html", data)