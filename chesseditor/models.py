

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import itertools

class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender_choice = (
       ('M', 'Mężczyzna'),
       ('F', 'Kobieta'),
       ('O', 'Inna'),
    )
    gender = models.CharField(max_length=1, choices=gender_choice, default='O')

    class Meta:
        abstract = True

    def __str__(self):
        return "{name} {surname}".format(name=self.name, surname=self.surname)


class Arbiter(Person):
    arbiter_id = models.AutoField(primary_key=True)  # unique and null=false


class Player(Person):
    player_id = models.AutoField(primary_key=True)  # unique and null=false


class Tournament(models.Model):
    tournament_id = models.AutoField(primary_key=True)
    name_of_tournament = models.CharField(max_length=50)
    date_of_start = models.DateField()
    date_of_end = models.DateField()
    place_of_tournament = models.CharField(max_length=50)
    max_nb_of_players = models.IntegerField(default=50)

    def __str__(self):
        return self.name_of_tournament


class Organizer(models.Model):
    organizer_id = models.AutoField(primary_key=True)  # unique and null=false
    name = models.CharField(max_length=30)
    tournament = models.ManyToManyField(Tournament)

    def __str__(self):
        return self.name


class ChessParty(models.Model):
    chessparty_id = models.AutoField(primary_key=True)
    arbiter = models.ForeignKey(Arbiter)
    white = models.ForeignKey(Player, related_name='something_white')
    black = models.ForeignKey(Player, related_name='something_black')
    tournament = models.ForeignKey(Tournament)

    def __str__(self):
        return "{chessparty_id}"\
            .format(chessparty_id=self.chessparty_id)


class State(models.Model):
    party = models.ForeignKey(ChessParty, default='0')
    chessman = (
        ('a1_w_rook', 'biała wieża a1'), ('h1_w_rook', 'biała wieża h1'),
        ('b1_w_knight', 'biały skoczek b1'), ('g1_w_knight', 'biały skoczek g1'),
        ('c1_w_bishop', 'biały goniec c1'), ('f1_w_bishop', 'biały goniec f1'),
        ('d1_w_queen', 'biały hetman d1'), ('e1_w_king', 'biały król e1'),
        ('a2_w_pawn', 'biały pion a2'), ('b2_w_pawn', 'biały pion b2'),
        ('c2_w_pawn', 'biały pion c2'), ('d2_w_pawn', 'biały pion d2'),
        ('e2_w_pawn', 'biały pion e2'), ('f2_w_pawn', 'biały pion f2'),
        ('g2_w_pawn', 'biały pion g2'), ('h2_w_pawn', 'biały pion h2'),
        ('a8_b_rook', 'czarna wieża a1'), ('h8_b_rook', 'czarna wieża h8'),
        ('b8_b_knight', 'czarny skoczek b1'), ('g8_b_knight', 'czarny skoczek g8'),
        ('c8_b_knight', 'czarny goniec c1'), ('f8_b_bishop', 'czarny goniec f8'),
        ('d8_b_queen', 'czarny hetman d1'), ('e8_b_king', 'czarny król e8'),
        ('a7_b_pawn', 'czarny pion a7'), ('b7_b_pawn', 'czarny pion b7'),
        ('c7_b_pawn', 'czarny pion c7'), ('d7_b_pawn', 'czarny pion d7'),
        ('e7_b_pawn', 'czarny pion e7'), ('f7_b_pawn', 'czarny pion f7'),
        ('g7_b_pawn', 'czarny pion g7'), ('h7_b_pawn', 'czarny pion h7'),
     )
    chessman = models.CharField(max_length=30, choices=chessman, default='pionek')
    mymove = []
    for a, b in itertools.product('abcdefgh', '12345678'):
        name = a + b
        mymove.append((name, name))
    mytuple = tuple(mymove)
    move = models.CharField(max_length=2, choices=mytuple, default='a1')
    is_capture = models.BooleanField(default=False)
    capture_choice = (
        ('true', 'zbity'),
        ('false', 'nie zbity'),
    )
    is_capture = models.CharField(max_length=9, choices=capture_choice, default='false')

class Moves(State):
    move_id = models.AutoField(primary_key=True)
    move_number = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "ruch nr:{move_number} partia pomiędzy:{party}" \
            .format(move_number=self.move_number, party=self.party)


