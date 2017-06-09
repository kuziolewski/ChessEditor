

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import itertools

class Person(models.Model):
    name = models.CharField("Imię", max_length=20)
    surname = models.CharField("Nazwisko", max_length=50)
    date_of_birth = models.DateField("Data Urodzenia", auto_now=False, auto_now_add=False)
    gender_choice = (
       ('M', 'Mężczyzna'),
       ('F', 'Kobieta'),
       ('O', 'Inna'),
    )
    gender = models.CharField("Płeć", max_length=1, choices=gender_choice, default='O')

    class Meta:
        abstract = True

    def __str__(self):
        return "{name} {surname}".format(name=self.name, surname=self.surname)


class Arbiter(Person):
    arbiter_id = models.AutoField(primary_key=True)  # unique and null=false

    class Meta:
        verbose_name = "Sędziego"
        verbose_name_plural = "Sędziowie"


class Player(Person):
    player_id = models.AutoField(primary_key=True)  # unique and null=false

    class Meta:
        verbose_name = "Gracz"
        verbose_name_plural = "Zawodnicy"


class Organizer(models.Model):
    organizer_id = models.AutoField("ID organizatora", primary_key=True)  # unique and null=false
    name = models.CharField("Nazwa organizatora: ", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Organizatora"
        verbose_name_plural = "Organizatorzy"


class Tournament(models.Model):
    tournament_id = models.AutoField("ID turnieju", primary_key=True)
    name_of_tournament = models.CharField("Nazwa turnieju", max_length=50)
    date_of_start = models.DateField("Data startu")
    date_of_end = models.DateField("Data zakończenia")
    place_of_tournament = models.CharField("Miejsce turnieju", max_length=50)
    max_nb_of_players = models.IntegerField("Liczba uczetników", default=50)
    organizer_of_tournament = models.ForeignKey(Organizer, verbose_name="Organizator turnieju")

    def __str__(self):
        return self.name_of_tournament

    class Meta:
        verbose_name = "Turniej"
        verbose_name_plural = "Turnieje"


class ChessParty(models.Model):
    chessparty_id = models.AutoField("ID partii", primary_key=True)
    arbiter = models.ForeignKey(Arbiter, related_name='sedzia', verbose_name="Sędzia")
    white = models.ForeignKey(Player, related_name='Białe', verbose_name="Białe figury")
    black = models.ForeignKey(Player, related_name='Czarne', verbose_name="Czarne figury")
    tournament = models.ForeignKey(Tournament, verbose_name="Nazwa turnieju")

    def __str__(self):
        return "{white} vs {black}, ({tournament})"\
            .format(black=self.black, white=self.white, tournament=self.tournament)

    class Meta:
        verbose_name = "Partia"
        verbose_name_plural = "Partie"


class OneMove(models.Model):
    party = models.ForeignKey(ChessParty, default='0', verbose_name="Partia")
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
    chessman = models.CharField(max_length=30, choices=chessman, default='pionek', verbose_name="Figura Szachowa")
    mymove = []
    for a, b in itertools.product('abcdefgh', '12345678'):
        name = a + b
        mymove.append((name, name))
    mytuple = tuple(mymove)
    move = models.CharField(max_length=2, choices=mytuple, default='a1', verbose_name="Ruch na")

    class Meta:
        abstract = True


class State(OneMove):
    state_id = models.PositiveIntegerField(default=0, verbose_name="numer ruchu")
    is_capture = models.BooleanField(default=False, verbose_name="Czy zbita")
    capture_choice = (
        ('true', 'zbity'),
        ('false', 'nie zbity'),
    )
    is_capture = models.CharField(max_length=9, choices=capture_choice, default='false', verbose_name="Czy zbity")

    def __str__(self):
        return "ruch nr:{state_id} partia pomiędzy:{party}, figura: {chessman}" \
            .format(party=self.party, state_id=self.state_id, chessman=self.chessman)

    class Meta:
        verbose_name = "Stan"
        verbose_name_plural = "Aktualne Stany Partii"


class Moves(OneMove):
    move_id = models.AutoField(primary_key=True)
    move_number = models.PositiveIntegerField(default=1, verbose_name="Numer ruchu w partii")

    def __str__(self):
        return "ruch nr:{move_number} partia pomiędzy:{party}" \
            .format(move_number=self.move_number, party=self.party)

    class Meta:
        verbose_name = "Ruch"
        verbose_name_plural = "Ruchy"
