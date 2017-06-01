from django.shortcuts import render, get_object_or_404
from .models import Arbiter, Tournament, Player, Organizer, State, Moves, ChessParty


def index(request):
    tournaments = Tournament.objects.all().order_by('-date_of_start')
    return render(request, 'chesseditor/index.html', {'tournaments': tournaments})


def turniej(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    chessparty = ChessParty.objects.filter(tournament=tournament)
    moves = Moves.objects.all()
    return render(request, 'chesseditor/turniej.html', {'tournament': tournament,\
                                                        'chesspartys': chessparty, 'moves': moves})


def rozgrywka(request, pk):
    chessparty = get_object_or_404(ChessParty, pk=pk)
    moves = Moves.objects.filter(party=chessparty)
    return render(request, 'chesseditor/rozgrywka.html', {'chessparty': chessparty, 'moves': moves})


def edytor(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    player = Player.objects.all()
    arbiter = Arbiter.objects.all()
    state = State.objects.all()
    organizer = Organizer.objects.all()
    return render(request, 'chesseditor/edytor.html', {'tournament': tournament, 'player': player, 'arbiter': arbiter,\
                                                       'state': state, 'organizer': organizer})
