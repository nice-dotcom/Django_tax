from django.db import models
from django import forms

class Question:
    def __init__(self, text, yes_node=None, no_node=None):
        self.text = text
        self.yes_node = yes_node
        self.no_node = no_node

question_10 = Question("Keine Auswanderung sinnvoll")
question_9 = Question("Keine Auswanderung sinnvoll")
question_8 = Question("Kein PP kommt in Frage")
question_7 = Question("PP kommt in Frage")
question_6 = Question("Auswanderung mit festem Wohnsitz kommt in Frage, bitte informiere dich bei unseren Experten")
question_5 = Question("PP kommt generell in Frage, informiere bei unseren Experten")
question_4 = Question("Kannst du die Bezugspunkte auflösen?", yes_node=question_7, no_node=question_8)
question_3 = Question("Kannst du dir vorstellen im Ausland fest in einem Land zu leben?", yes_node=question_6, no_node=question_9)
question_2 = Question("Hattest du Bezugspunkte zu Deutschland wie Kinder, Frau oder Wohnung mit Schlüsselgewalt?", yes_node=question_4, no_node=question_5)
question_1 = Question("Kannst du dir vorstellen in 3 Ländern zu leben und dabei weniger als 183 Tage im Jahr pro Land zu bleiben?", yes_node=question_2, no_node=question_3)
question_0 = Question("Möchtest du auswandern?", yes_node=question_1, no_node=question_10)  # Start node



FRUIT_CHOICES= [
    ('yes', 'Ja'),
    ('no', 'Nein'),
    ]

class Button(forms.Form):
    antwort = forms.CharField(label='Anwort bitte:', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
