from django import forms
from .models import Arbiter, Tournament, Player, Organizer, State, Moves, ChessParty


class ChessPartyForm(forms.ModelForm):

    class Meta:
        model = ChessParty
        fields = ('arbiter', 'white', 'black')


class GameForm(forms.ModelForm):

    class Meta:
        model = Moves
        fields = ('chessman', 'move', 'move_number', 'party')


