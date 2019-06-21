from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Item


def home(request):
    return render(request, 'home.html')

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'
   

class ItemList(ListView):
    model = Item
    

class ItemDetail(DetailView):
    model = Item


class ItemDelete(DeleteView):
    model = Item
    success_url = '/'
   