from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()


class Board(models.Model):
    PRIVATE = 'pr'
    PUBLIC = 'pu'

    VISIBILITY_TYPES = (
        (PRIVATE, 'private'),
        (PUBLIC, 'public'),
    )
    title = models.CharField(max_length=100, verbose_name='Тактанын аты')
    visibility = models.CharField(max_length=2, choices=VISIBILITY_TYPES, default=PRIVATE)
    creator = models.ForeignKey(User, related_name='boards', on_delete=models.CASCADE, blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    assign_users = models.ManyToManyField(User, related_name='assign_boards', blank=True)
    
    def __str__(self) -> str:
        return self.title


class List(models.Model):
    title = models.CharField(max_length=100, verbose_name='Баракчанын аты')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    creator = models.ForeignKey(User, related_name='lists', on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Card(models.Model):
    WATCH = 'w'
    NOT_WATCH = 'nw'

    NOTIFICATIONS_STATUS = (
        (WATCH, 'w'),
        (NOT_WATCH, 'nw'),
    )

    title = models.CharField(max_length=100, verbose_name='Тапшырманын аты')
    create_at = models.DateField(auto_now_add=True)
    description = models.TextField(verbose_name='Суроттомо')
    tag = models.CharField(max_length=150, verbose_name='тэг', blank=True)
    notification_status = models.CharField(max_length=2, choices=NOTIFICATIONS_STATUS, default=NOT_WATCH)

    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cardsCreate', null=True)
    deadline = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='deadline')
    assign_user = models.ManyToManyField(User, related_name='assign_cards', blank=True)
    # complete = models.BooleanField(default=False)

    def __str__(self):
        return f'CardId: {self.id} | listId: {self.list.id} | {self.creator}'
    
    # def complete_task(self):
    #     self.complete = True
    #     self.save()

class Comment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    text = models.TextField()
    writed_at = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writerComments')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='comments')
    replyComment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)
    replyCommentId = models.IntegerField(editable=False, null=True, validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['-writed_at']


