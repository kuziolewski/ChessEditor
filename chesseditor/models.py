
from django.utils.safestring import mark_safe
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import itertools

class Person(models.Model):
    name = models.CharField("Imię", max_length=20)
    surname = models.CharField("Nazwisko", max_length=50)
    date_of_birth = models.DateField("Data Urodzenia", auto_now=False, auto_now_add=False)
    GENDER_CHOICES = (
       ('M', 'Mężczyzna'),
       ('F', 'Kobieta'),
       ('O', 'Inna'),
    )
    gender = models.CharField("Płeć", max_length=1, choices=GENDER_CHOICES, default='O')

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
        return "{white} vs {black}, ({tournament}),partia nr {chessparty_id}"\
            .format(black=self.black, white=self.white, tournament=self.tournament, chessparty_id=self.chessparty_id)

    class Meta:
        verbose_name = "Partia"
        verbose_name_plural = "Partie"

    def save(self, *args, **kwargs):
        super(ChessParty, self).save(*args, **kwargs)
        State.objects.create(party_id=self.pk, chessman='biała wieża a1', move='a1', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biała wieża h1', move='h1', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały skoczek b1', move='b1', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały skoczek g1', move='g1', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały goniec c1', move='c1', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały goniec f1', move='f1', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały hetman d1', move='d1', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały król e1', move='e1', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały pion a2', move='a2', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały pion b2', move='b2', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały pion c2', move='c2', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały pion d2', move='d2', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały pion e2', move='e2', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały pion f2', move='f2', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały pion g2', move='g2', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='biały pion h2', move='h2', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarna wieża a8', move='a8', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarna wieża h8', move='h8', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny skoczek b8', move='b8', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny skoczek g8', move='g8', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny goniec c8', move='c8', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny goniec f8', move='f8', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny hetman d8', move='d8', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny król e8', move='e8', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny pion a7', move='a7', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny pion b7', move='b7', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny pion c7', move='c7', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny pion d7', move='d7', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny pion e7', move='e7', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny pion f7', move='f7', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny pion g7', move='g7', state_id='0', is_capture='false')
        State.objects.create(party_id=self.pk, chessman='czarny pion h7', move='h7', state_id='0', is_capture='false')


class OneMove(models.Model):
    party = models.ForeignKey(ChessParty, default='0', verbose_name="Partia", blank=True, null=True)
    CHESSMAN_CHOICES = (
        ('biała wieża a1', mark_safe('&#9814;')), ('biała wieża h1', mark_safe('&#9814;')),
        ('biały skoczek b1', mark_safe('&#9816;')), ('biały skoczek g1', mark_safe('&#9816;')),
        ('biały goniec c1', mark_safe('&#9815;')), ('biały goniec f1', mark_safe('&#9815;')),
        ('biały hetman d1', mark_safe('&#9813;')), ('biały król e1', mark_safe('&#9812;')),
        ('biały pion a2', mark_safe('&#9817;')), ('biały pion b2', mark_safe('&#9817;')),
        ('biały pion c2', mark_safe('&#9817;')), ('biały pion d2', mark_safe('&#9817;')),
        ('biały pion e2', mark_safe('&#9817;')), ('biały pion f2', mark_safe('&#9817;')),
        ('biały pion g2', mark_safe('&#9817;')), ('biały pion h2', mark_safe('&#9817;')),
        ('czarna wieża a8', mark_safe('&#9820;')), ('czarna wieża h8', mark_safe('&#9820;')),
        ('czarny skoczek b8', mark_safe('&#9822;')), ('czarny skoczek g8', mark_safe('&#9822;')),
        ('czarny goniec c8', mark_safe('&#9821;')), ('czarny goniec f8', mark_safe('&#9821;')),
        ('czarny hetman d8', mark_safe('&#9813;')), ('czarny król e8', mark_safe('&#9818;')),
        ('czarny pion a7', mark_safe('&#9823;')), ('czarny pion b7', mark_safe('&#9823;')),
        ('czarny pion c7', mark_safe('&#9823;')), ('czarny pion d7', mark_safe('&#9823;')),
        ('czarny pion e7', mark_safe('&#9823;')), ('czarny pion f7', mark_safe('&#9823;')),
        ('czarny pion g7', mark_safe('&#9823;')), ('czarny pion h7', mark_safe('&#9823;')),
     )
    chessman = models.CharField(max_length=30, choices=CHESSMAN_CHOICES, default='pionek', verbose_name="Figura Szachowa")
    mymove = []
    for a, b in itertools.product('abcdefgh', '12345678'):
        name = a + b
        mymove.append((name, name))
    MYTUPLE = tuple(mymove)
    move = models.CharField(max_length=2, choices=MYTUPLE, default='a1', verbose_name="Ruch na")

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
        return mark_safe("ruch nr:{state_id} partia pomiędzy:{party}, figura: {chessman}, aktualne pole: {move}"\
            .format(party=self.party, state_id=self.state_id,  chessman=self.get_chessman_display(), move=self.move))

    class Meta:
        verbose_name = "Stan"
        verbose_name_plural = "Aktualny Stan Parti"


class Moves(OneMove):
    move_id = models.AutoField(primary_key=True)  #
    move_number = models.PositiveIntegerField(default=1, verbose_name="Numer ruchu w partii")

    def __str__(self):
        return mark_safe("ruch nr:{move_number} partia pomiędzy:{party}, figura: {chessman}" \
            .format(move_number=self.move_number, party=self.party, chessman=self.chessman))
#get_chessman_display
    class Meta:
        verbose_name = "Ruch"
        verbose_name_plural = "Ruchy"

    def save(self, *args, **kwargs):
        super(Moves, self).save(*args, **kwargs)
        State.objects.filter(chessman=self.chessman).update(move=self.move);
        #State.objects.create(party_id=self.party_id, chessman=self.chessman, move=self.move, state_id=self.move_number, is_capture='false')

