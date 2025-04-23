from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm

def home(request):
    people = Person.objects.all()
    return render(request, 'people/home.html', {'people': people})

def create(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'people/form.html', {'form': form})

def update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'people/form.html', {'form': form})

def delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('home')
