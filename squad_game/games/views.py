from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Game
from django.contrib import messages

def template(request):
    return render(request, 'games/template.html')

def index(request):
    return render(request, 'games/base.html')

@login_required
def create_game(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        game = Game.objects.create(
            title=title, author=request.user
        )
        messages.success(request, f'Game created. You can invite your friends with the code: {game.code}')
        return redirect(f'/games/game/{game.code}')
    return render(request, 'games/create.html')


@login_required
def join_game(request):
    game_code = request.GET.get("code")
    try:
        game = Game.objects.get(code=game_code)
    except Game.DoesNotExist:
        messages.error(request, 'Game does not exist')
        return redirect('/')
    else:
        return redirect(f'/games/game/{game.code}')


@login_required
def detail_game(request, code):
    try:
        game = Game.objects.get(code=code)
    except Game.DoesNotExist:
        messages.error(request, 'Game does not exist')
        return redirect('/')
    else:
        return render(request, 'games/game.html', {'game': game})