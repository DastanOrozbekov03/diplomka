from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView 
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Board, List, Card, Comment


class BoardCreateView(LoginRequiredMixin ,CreateView):
    model = Board
    fields = ['title', 'visibility', 'assign_users']
    success_url = reverse_lazy('board_list')
    template_name = 'task_manager/board_form.html' 

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'task_manager/not_authenticated.html')
        return super().dispatch(request, *args, **kwargs)
 

class BoardListView(ListView):
    model = Board
    context_object_name = 'boards'
    template_name =  'task_manager/board_list.html'


class BoardDeleteView(DeleteView):
    model = Board
    context_object_name = 'board'
    success_url = reverse_lazy('board_list')

class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    fields = ['title', 'board', 'creator']
    success_url = reverse_lazy('list_list')
    template_name = 'task_manager/list_form.html'     

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'task_manager/not_authenticated.html')
        return super().dispatch(request, *args, **kwargs)

def list_list(request):
    lists = List.objects.all()
    print(lists)
    return render(request,'task_manager/list_list.html',{'lists':lists})


class ListListView(ListView):
    model = List
    context_object_name = 'lists'
    template_name = 'task_manager/list_list.html'

    def get_queryset(self):
        # Возвращаем список всех списков, связанных с текущим пользователем
        return List.objects.filter(creator=self.request.user)

class ListDeleteView(DeleteView):
    model = List
    context_object_name = 'list'
    success_url = reverse_lazy('list_list')


class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['title', 'description', 'tag', 'notification_status', 'list', 'creator']
    template_name = 'task_manager/card_form.html'
    success_url = reverse_lazy('list_list')


    def form_valid(self, form):
        # Получить объект списка на основе переданного идентификатора (полученного из URL)
        list_id = self.kwargs['list_id']
        list_obj = get_object_or_404(List, id=list_id)
        # Установить список для карточки
        form.instance.list = list_obj
        # Установить создателя карточки
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'task_manager/not_authenticated.html')
        return super().dispatch(request, *args, **kwargs)
class CardListView(ListView):
    model = Card
    context_object_name = 'cards'  
    template_name = 'task_manager/list_list.html'

class CardDeleteView(DeleteView):
    model = Card
    context_object_name = 'card'
    success_url = reverse_lazy('list_list')

