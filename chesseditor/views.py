from django.shortcuts import render, get_object_or_404
from .models import Arbiter, Tournament, Player, Organizer, States, Moves, ChessParty


def index(request):
    tournaments = Tournament.objects.all()
    return render(request, 'chesseditor/index.html', {'tournaments': tournaments})


def edit(request):
    return render(request, 'chesseditor/edit.html', {})


def show(request):
    return render(request, 'chesseditor/show.html', {})


def turniej(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    chesspartys = ChessParty.objects.filter(tournament=tournament)
    return render(request, 'chesseditor/turniej.html', {'tournament': tournament, 'chesspartys': chesspartys})