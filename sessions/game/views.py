from random import random

from django.shortcuts import render
from .models import Player, Game
from .forms import GameForm

MAX_ATTEMPTS = 3
MIN_VALUE = 1
MAX_VALUE = 9


def play(game, player, current_value):
    context = {'attempts': MAX_ATTEMPTS - game.current_attempt,
               'current_attempt': game.current_attempt,
               'current_value': current_value}

    if player == game.player1:
        context['player1'] = True
        if game.correct_value is None:
            game.correct_value = random.randint(MIN_VALUE, MAX_VALUE)
            game.save()
        context['correct_value'] = game.correct_value
    else:
        context['player1'] = False
        if not game.is_over:
            if MAX_ATTEMPTS == game.current_attempt:
                if game.correct_value == current_value:
                    game.is_over = True
                    game.is_value_found = True
                else:
                    context['values_comparison'] = 'more' if current_value > game.correct_value else 'less'
                    game.current_attempt += 1
    context['game_is_over': game.is_over]
    context['is_value_found': game.is_value_found]
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


    print(context)
    return render(request, 'game.html', context)
