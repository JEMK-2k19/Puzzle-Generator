from django.shortcuts import render
from . import forms
from . import carpark_logic
from datetime import datetime

# Create your views here.
'''
def carpark_view(request):
    output = []
    if request.method == "POST":
        form = forms.RouteForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data['start']
            dest = form.cleaned_data['destination']
            now = str(datetime.now())
            output = [carpark_logic.find_nearest_carpark(dest)]
    else:
        form = forms.RouteForm()
    return render(request, 'carpark/carpark.html', {'form': form, 'output': output})
'''

def new_view(request):
    return render(request, 'carpark/new.html')

def new_game(request):
    if request.method == "POST":
        form = forms.NewGameForm(request.POST)
        words = form.words
        if form.is_valid():
            source = form.cleaned_data['answer']
            if source == form.answer:
                form = forms.AnswerForm(request.POST)
                output = ["correct"]
            else:
                output = ["Wrong answer"]
    else:
        form = forms.AnswerForm()
        words = form.words
    return render(request, 'carpark/new_game.html', {'form': form, 'words': words})

def join_game(request):
    return render(request, 'carpark/join_game.html')

def read_csv(fname):
    new = []
    with open(fname, encoding = 'utf-8') as f:
        for row in csv.reader(f):
            new.append(row)
    return new

def quiz(request):
    output = []
    if request.method == "POST":
        form = forms.AnswerForm(request.POST)
        words = form.words
        if form.is_valid():
            source = form.cleaned_data['answer']
            if source == form.answer:
                form = forms.AnswerForm(request.POST)
                output = ["correct"]
            else:
                output = ["Wrong answer"]
    else:
        form = forms.AnswerForm()
        words = form.words
    return render(request, 'carpark/quiz.html', {'form': form, 'words': words, 'output': output})
