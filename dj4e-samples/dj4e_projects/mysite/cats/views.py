from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import Cat, Breed


class CatsList(LoginRequiredMixin, View):
    def get(self, request):
        cat_models = Cat.objects.all()
        breed_count = Breed.objects.all().count()
        ctx = {"models": cat_models, "breed_count": breed_count}
        return render(request, template_name="cats/cat_list.html", context=ctx)


class BreedList(LoginRequiredMixin, View):
    def get(self, request):
        breed_models = Breed.objects.all()
        ctx = {"models": breed_models}
        return render(request, template_name="cats/breed_list.html", context=ctx)


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:all')


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:all')
