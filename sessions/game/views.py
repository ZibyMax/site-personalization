from django.shortcuts import render
from .models import Player, Game

ATTEMPTS = 3
MIN_NUMBER = 1
MAX_NUMBER = 9


def play(player):
    pass


def show_result(player):
    pass


def play_the_game(request):
    player_id = request.session.get('player_id', None)
    if player_id:
        player = Player.objects.get(id=player_id)
        games = Game.objects.filter(player1=player, player2=player)
        if games.exist():
            active_game = games.filter(is_active=True)
            if active_game.exist():
                game = active_game.last()
                play(game)
            else:
                game = games.last()
                show_result(game)
    else:
        player = Player()
        player.save()
        request.session['player_id'] = player.id
        games = Game.objects.filter(player2=None)
        if games.exist():
            game = games.last()
            game.player2 = player
        else:
            game = Game()
            game.player1 = player
        game.save()
        play(game)

    return render(request, 'game.html')

