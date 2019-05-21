from django.db import models


class Player(models.Model):
    pass


class Game(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='+', default=None, null=True)
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='+', default=None, null=True)
    is_over = models.BooleanField(default=False)
    is_value_found = models.BooleanField(default=False)
    current_attempt = models.IntegerField(default=0)
    correct_value = models.IntegerField(null=True)


# class PlayerGameInfo(models.Model):
#     pass
