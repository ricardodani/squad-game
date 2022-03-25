from django.shortcuts import render

def template(request):
    return render(request, 'games/template.html')