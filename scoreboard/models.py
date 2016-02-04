# coding=utf-8
from django.db import models


class Score(models.Model):
    player_choices = (
        ("何", "何"),
        ("余", "余"),
        ("张", "张"),
    )
    winner = models.CharField("胜者", choices=player_choices, max_length=50, default="何")
    loser = models.CharField("负者", choices=player_choices, max_length=50, default="余")
    time = models.DateTimeField("比赛时间", auto_now_add=True)
