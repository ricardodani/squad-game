from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def template(request):
    return render(request, 'games/template.html')

def index(request):
    return render(request, 'games/base.html')

@login_required
def create_game(request):
    return render(request, 'games/base.html')