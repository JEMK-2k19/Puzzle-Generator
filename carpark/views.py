from django.shortcuts import render
from . import forms
from .models import CurrentRound, Game
from . import WordGenerator
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
    round = CurrentRound.objects.last()
    if round.question_no > 3:
        return render(request, 'endgame.html', {'points': [round.points]})
    output = []
    form = forms.AnswerForm(request.POST)
    links = [round.link1, round.link2]
    words = [round.word1, round.word2]
    points = [round.points]
    answer = round.answer
    if form.is_valid():
        source = form.cleaned_data['answer']
        if source == answer:
            update_round()
            round = CurrentRound.objects.last()
            points = [round.points]
            links = [round.link1, round.link2]
            form = forms.AnswerForm()
            output = ["Previous answers: " + words[0] + ", " + words[1]]
        else:
            form = forms.AnswerForm()
            output = ["Wrong answer"]
    return render(request, 'carpark/quiz.html', {'form': form, 'links': links, 'words': words, 'output': output,
                                                 'points' : points})

def update_round():
    round = CurrentRound.objects.last()
    puzzle = WordGenerator.Puzzle()
    links = puzzle.links
    round.link1 = links[0]
    round.link2 = links[1]
    words = puzzle.words
    round.word1 = words[0]
    round.word2 = words[1]
    round.answer = puzzle.answer
    round.question_no += 1
    round.points += 20
    round.save()

def init_quiz(request):
    output = []
    form = forms.AnswerForm()
    puzzle = WordGenerator.Puzzle()
    links = puzzle.links
    words = puzzle.words
    answer = puzzle.answer
    round = CurrentRound(word1=words[0], word2=words[1], answer=answer, points=0, question_no=0,
                         link1=links[0], link2=links[1])
    round.save()
    return render(request, 'carpark/quiz.html', {'form': form, 'links': links, 'words': [], 'output': output})

def give_up(request):
    form = forms.AnswerForm()
    round = CurrentRound.objects.last()
    words = [round.word1, round.word2]
    output = ["Previous answers: " + words[0] + ", " + words[1]]
    update_round()
    links = [round.link1, round.link2]
    points = [round.points]
    return render(request, 'carpark/quiz.html', {'form': form, 'links': links, 'words': words, 'output': output,
                                             'points': points})
