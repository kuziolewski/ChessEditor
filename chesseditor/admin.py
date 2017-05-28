from django.contrib import  admin

from .models import Player, Arbiter, Organizer, Move, ChessParty, Tournament
# Register your models here.


admin.site.register([Player, Arbiter, Organizer, Move, ChessParty, Tournament])
