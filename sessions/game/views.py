from random import random

from django.shortcuts import render
from .models import Player, Game
from .forms import GameForm

MAX_ATTEMPTS = 3
MIN_VALUE = 1
MAX_VALUE = 9


def play(game, player, current_value):
    context = {'player1': False,
               'is_over': game.is_over,
               'is_is_value_found': game.is_value_found,
               'current_attempt': game.current_attempt,
               'min_value': MIN_VALUE,
               'max_value': MAX_VALUE,
               'attempts': MAX_ATTEMPTS - game.current_attempt}

    if player == game.player1:
        context['player1'] = True
        if game.correct_value is None:
            game.correct_value = random.randint(MIN_VALUE, MAX_VALUE)
            game.save()
        context['correct_value'] = game.correct_value
    else:
        if not game.is_over:
            pass

    return context


def play_the_game(request):
    player_id = request.session.get('player_id', None)
    if player_id:
        player = Player.objects.get(id=player_id)
        game = Game.objects.filter(player1=player, player2=player).first()
    else:
        player = Player()
        player.save()
        request.session['player_id'] = player.id
        game = Game.objects.filter(player2=None).first()
    if not game:
        game = Game()
        game.player1 = player
    else:
        game.player2 = player
    game.save()

    current_value = None
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            current_value = form.cleaned_data['value']
    else:
        form = GameForm()

    if game:
        context = play(game, player, current_value)
        context['form'] = form
    else:
        context = {'error': '"Этого не может быть!'}



    return render(request, 'game.html', context)
