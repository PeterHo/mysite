from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from scoreboard.forms import ScoreForm
from scoreboard.models import Score


def scores(request):
    if request.POST:
        form = ScoreForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['winner'] != form.cleaned_data['loser']:
                form.save()
            return redirect("score:scores")

    h_win = Score.objects.filter(winner='何').count()
    h_lose = Score.objects.filter(loser='何').count()
    h_score = (h_win - h_lose) * 3

    y_win = Score.objects.filter(winner='余').count()
    y_lose = Score.objects.filter(loser='余').count()
    y_score = (y_win - y_lose) * 3

    z_win = Score.objects.filter(winner='张').count()
    z_lose = Score.objects.filter(loser='张').count()
    z_score = (z_win - z_lose) * 3

    ctx = {
        'form': ScoreForm,
        'players': [
            {
                'name': '何',
                'win': h_win,
                'lose': h_lose,
                'score': h_score,
            },
            {
                'name': '余',
                'win': y_win,
                'lose': y_lose,
                'score': y_score,
            },
            {
                'name': '张',
                'win': z_win,
                'lose': z_lose,
                'score': z_score,
            },
        ]
    }
    ctx.update(csrf(request))
    return render(request, 'scores.html', ctx)
