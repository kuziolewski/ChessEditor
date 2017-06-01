from django.contrib import  admin

from .models import Player, Arbiter, Organizer, Moves, ChessParty, Tournament, State
# Register your models here.e


admin.site.register([Player, Arbiter, Organizer, Moves, ChessParty, Tournament, State])
