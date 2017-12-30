from django.shortcuts import render, get_object_or_404
from .models import Board

def home(request):
    boards = Board.objects.all()

    response_data = {
        'boards': boards
    }
    return render(request, 'home.html', response_data)

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)

    response_data = {
        'board': board
    }
    return render(request, 'topics.html', response_data)
