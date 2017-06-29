from django.shortcuts import render, get_object_or_404
from .models import Arbiter, Tournament, Player, Organizer, State, Moves, ChessParty
from .forms import ChessPartyForm, GameForm
from django.shortcuts import redirect
from django.utils.safestring import mark_safe

def index(request):
    tournaments = Tournament.objects.all().order_by('-date_of_start')
    return render(request, 'chesseditor/index.html', {'tournaments': tournaments})


def turniej(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    chesspartys = ChessParty.objects.filter(tournament=tournament)
    moves = Moves.objects.all()
    return render(request, 'chesseditor/turniej.html', {'tournament': tournament,\
                                                        'chesspartys': chesspartys, 'moves': moves})


def rozgrywka(request, pk):
    chessparty = get_object_or_404(ChessParty, pk=pk)
    moves = Moves.objects.filter(party=chessparty)
    states = State.objects.filter(party=chessparty)
    return render(request, 'chesseditor/rozgrywka.html', {'chessparty': chessparty, 'moves': moves, 'states': states})


def edytor(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    players = Player.objects.all()
    arbiters = Arbiter.objects.all()
    organizers = Organizer.objects.all()
    chesspartys = ChessParty.objects.all()
    states = State.objects.all()
    form = ChessPartyForm()
    if request.method == "POST":
        form = ChessPartyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.tournament = tournament
            post.save(force_insert=True)
            return redirect('gra', pk=post.pk)
    return render(request, 'chesseditor/edytor.html', {'tournament': tournament, 'players': players, 'arbiters': arbiters,\
                                                       'states': states, 'organizers': organizers, 'form': form, 'chesspartys': chesspartys})


def gra(request, pk):
    chessparty = get_object_or_404(ChessParty, pk=pk)
    moves = Moves.objects.filter(party=chessparty)
    states = State.objects.filter(party=chessparty)
    if request.method == "POST":
        form = mark_safe(GameForm(request.POST))
        if form.is_valid():
            post = form.save(commit=False)
            post.chessparty=pk;
            post.save(force_insert=True)
    else:
        form = GameForm()
    return render(request, 'chesseditor/gra.html', {'chessparty': chessparty, 'moves': moves, 'form': form, 'states': states})