from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    """Model definition for Board."""

    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'

    def __str__(self):
        return self.name

class Topic(models.Model):
    """Model definition for Topic."""

    subject = models.CharField(max_length=100)
    board = models.ForeignKey(Board, related_name='topics')
    last_updated = models.DateTimeField(auto_now_add=True)
    starter = models.ForeignKey(User, related_name='topics')

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    def __str__(self):
        return self.subject

class Post(models.Model):
    """Model definition for Post."""

    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        pass

