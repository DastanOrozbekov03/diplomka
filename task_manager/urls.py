from django.urls import path
from .views import (BoardCreateView, BoardListView, BoardDeleteView, 
                    ListCreateView, CardListView, ListDeleteView,
                      CardCreateView,  CardDeleteView, list_list)
# from account.views import user_login

urlpatterns = [
  path('board/create/', BoardCreateView.as_view(), name='board_create'),
  path('', BoardListView.as_view(), name='board_list'),
  path('board/delete/<int:pk>/', BoardDeleteView.as_view(), name='board_delete'),
  path('list/create/', ListCreateView.as_view(), name='list_create'),
  path('list/list/', list_list, name='list_list'),
  path('list/delete/<int:pk>/', ListDeleteView.as_view(), name='list_delete'),
  path('card/create/<int:list_id>/', CardCreateView.as_view(), name='card_create'),
  path('card/list/', CardListView.as_view(), name='card_list'),
  path('card/delete/<int:pk>/', CardDeleteView.as_view(), name='card_delete'),
  # path('login/', user_login, name='user_login')
   
]