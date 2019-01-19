from django.shortcuts import render
from . import forms
# Create your views here.

def new_view(request):
    return render(request, 'carpark/new.html')

def new_game(request):
    return render(request, 'carpark/new_game.html')

def join_game(request):
    return render(request, 'carpark/join_game.html')

def quiz(request):
    output = []
    if request.method == "POST":
        form = forms.AnswerForm(False, request.POST)
        links = form.links
        words = form.words
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
    else:
        form = forms.AnswerForm(False)
        links = form.links
        words = []
    return render(request, 'carpark/quiz.html', {'form': form, 'links': links, 'words': words, 'output': output})
