from django import forms
from . import models
from . import WordGenerator

class RouteForm(forms.ModelForm):
    class Meta:
        model = models.Route
        fields = ["start", "destination"]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ["answer"]

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)

        # set the user_id as an attribute of the form
        self.puzzle = WordGenerator.Puzzle()
        self.words = self.puzzle.words
        self.answer = self.puzzle.answer

class NewGameForm(forms.ModelForm):
    class Meta:
        model = models.NewGameForm
        name = ["name"]

    def __init__(self, *args, **kwargs):
        super(NewGameForm, self).__init__(*args, **kwargs)

        # set the user_id as an attribute of the form
        self.puzzle = WordGenerator.Puzzle()
        self.words = self.puzzle.words
        self.answer = self.puzzle.answer