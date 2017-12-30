from django.shortcuts import render
from .models import Board

def home(request):
    boards = Board.objects.all()

    response_data = {
        'boards': boards
    }
    return render(request, 'home.html', response_data)
