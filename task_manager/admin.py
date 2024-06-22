from django.contrib import admin
from .models import Board, Card, List, Comment 


admin.site.register(Board)
admin.site.register(Card)
admin.site.register(List)
admin.site.register(Comment)