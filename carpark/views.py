from django.shortcuts import render
from . import forms
from .models import CurrentRound, Game
# Create your views here.

def wait_page(request):
    #persons = Articles.objects.raw('SELECT * FROM persons')
    #add persons as the second argument
    return render(request, 'carpark/wait_page.html')

def new_view(request):
    return render(request, 'carpark/new.html')

def new_game(request):
    if request.method == "POST":
        form = forms.CreatePerson(request.POST)
        game = Game.create("123")
        if form.is_valid():
            player_name = form.cleaned_data['name']

            return render(request, 'carpark/wait_page.html', {'game_id': game.game_id})
    else:
        form = forms.CreatePerson()
    return render(request, 'carpark/new_game.html', {'form': form})

def join_game(request):
    if request.method == "POST":
        form = forms.createJoinGameForm(request.POST)
        if form.is_valid():
            player_name = form.cleaned_data['name']
            access_code = form.cleaned_data['access_code']

            return render(request, 'carpark/wait_page.html')
    else:
        form = forms.createJoinGameForm()
    return render(request, 'carpark/join_game.html', {'form': form})

def quiz(request):
    if request.method != "POST":
        return init_quiz(request)
    output = []
    form = forms.AnswerForm(False, request.POST)
    links = form.links
    words = [CurrentRound.objects.get(id=1).word1, CurrentRound.objects.get(id=1).word1]
    answer = form.answer
    if form.is_valid():
        source = form.cleaned_data['answer']
        if source == answer:
            form = forms.AnswerForm(True)
            links = form.links
            output = []
        else:
            form = forms.AnswerForm(False)
            links = form.links
            words = []
            output = ["Wrong answer"]
    return render(request, 'carpark/quiz.html', {'form': form, 'links': links, 'words': words, 'output': output})

def init_quiz(request):
    output = []
    form = forms.AnswerForm(False)
    links = form.links
    words = []
    round = CurrentRound(word1=form.words[0], word2=form.words[1], points=0)
    round.save()
    return render(request, 'carpark/quiz.html', {'form': form, 'links': links, 'words': words, 'output': output})

