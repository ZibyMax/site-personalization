from django.shortcuts import render
from .models import Player, Game

MAX_ATTEMPTS = 3
MIN_VALUE = 1
MAX_VALUE = 9


def play(game, player):
    if player == game.player1:
        pass
    return {}


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

    if game:
        context = play(game, player)
    else:
        context = {'error': '"Этого не может быть!'}

    return render(request, 'game.html', context)

