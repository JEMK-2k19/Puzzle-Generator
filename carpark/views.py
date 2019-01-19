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

def quiz(request):
    output = []
    if request.method == "POST":
        form = forms.AnswerForm(False, request.POST)
        words = form.words
        answer = form.answer
        if form.is_valid():
            source = form.cleaned_data['answer']
            if source == answer:
                form = forms.AnswerForm(True)
                words = form.words
                output = []
            else:
                form = forms.AnswerForm(False)
                words = form.words
                output = ["Wrong answer"]
    else:
        form = forms.AnswerForm(False)
        words = form.words
    return render(request, 'carpark/quiz.html', {'form': form, 'words': words, 'output': output})
