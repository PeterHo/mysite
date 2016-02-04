# coding=utf-8
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from scoreboard.models import Score

__author__ = 'peter'


class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields = ('winner', 'loser')
