from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Flowers


class FlowersListView(ListView):
    template_name = "flowers/flowers_list.html"
    model = Flowers


class FlowersDetailView(DetailView):
    template_name = "flowers/flowers_detail.html"
    model = Flowers


class FlowersCreateView(CreateView):
    template_name = "flowers/flowers_create.html"
    model = Flowers
    fields = ["name", "user", "description"]



class FlowersUpdateView(UpdateView):
    template_name = "flowers/flowers_update.html"
    model = Flowers
    fields = ["name", "user", "description"]



class FlowersDeleteView(DeleteView):
    template_name = "flowers/flowers_delete.html"
    model = Flowers
    success_url = reverse_lazy("flowers_list")