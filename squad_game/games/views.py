from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Game, GameCategory, GamePlayer
from django.contrib import messages

def template(request):
    return render(request, 'games/template.html')

def index(request):
    if request.user.is_authenticated:
        context = {
        'my_games': Game.objects.filter(author=request.user),
        'guest_games': Game.objects.filter(
            players__user=request.user).exclude(author=request.user
        )
    }
    else:
        context = {}
    return render(request, 'games/base.html', context)

@login_required
def create_game(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        game = Game.objects.create(
            title=title, author=request.user
        )
        game_player = GamePlayer.objects.create(
            game=game,
            user=request.user,
            is_accepted=True
        )
        messages.success(request, f'Game created. You can invite your friends with the code: {game.code}')
        return redirect(f'/games/game/{game.code}')
    return render(request, 'games/create.html')


@login_required
def create_category(request, code):
    try:
        game = Game.objects.get(code=code, status=Game.DRAFT)
    except Game.DoesNotExist:
        messages.error(request, 'Draft game does not exist')
    if request.method == 'POST':
        title = request.POST.get('title')
        category = GameCategory.objects.create(
            game=game, title=title
        )
        messages.success(request, f'Category {category} create with success.')
    return redirect(f'/games/game/{game.code}')


@login_required
def join_game(request):
    game_code = request.GET.get("name")
    try:
        game = Game.objects.get(code=game_code)
    except Game.DoesNotExist:
        messages.error(request, 'Game does not exist')
        return redirect('/')
    else:
        return redirect(f'/games/game/{game.code}')


@login_required
def guest_join_game(request, code):
    try:
        game = Game.objects.get(code=code)
    except Game.DoesNotExist:
        messages.error(request, 'Game does not exist')
        return redirect('/')
    if request.method == 'POST':
        GamePlayer.objects.create(
            user=request.user,
            game=game
        )
        messages.success(request, 'Player entered in game as guest')
    return redirect(f'/games/game/{game.code}')


@login_required
def detail_game(request, code):
    try:
        game = Game.objects.get(code=code)
    except Game.DoesNotExist:
        messages.error(request, 'Game does not exist')
        return redirect('/')
    else:
        return render(request, 'games/game.html', {
            'game': game,
            'categories': game.categories.all(),
            'players': game.players.all(),
            'is_guest': game.players.filter(user=request.user).exists()
        })