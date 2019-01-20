from django import forms
from . import models
from . import WordGenerator

class RouteForm(forms.ModelForm):
    class Meta:
        model = models.Route
        fields = ["start", "destination"]

puzzle = WordGenerator.Puzzle()

class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ["answer"]

    def __init__(self, new, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)

        # set the user_id as an attribute of the form
        global puzzle
        if new:
            puzzle = WordGenerator.Puzzle()
        self.puzzle = puzzle
        self.links = self.puzzle.links
        self.words = self.puzzle.words
        self.answer = self.puzzle.answer

<<<<<<< HEAD
# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = models.Person
#         fields = ["name"]



=======
class createJoinGameForm(forms.ModelForm):
    class Meta:
        model = models.joinGameForm
        fields = ["name", "access_code"]

class CreatePerson(forms.ModelForm):
    class Meta:
        model = models.Player
        fields = ["name"]
>>>>>>> de470c07a17ac4b553bc62545313fc1d69145865
