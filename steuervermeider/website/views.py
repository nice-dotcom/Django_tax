from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html")



class QuestionForm(forms.Form):
    answer = forms.ChoiceField(choices=[('yes', 'Ja'), ('no', 'Nein')], widget=forms.RadioSelect)


def berater(request, question_number):
    questions = [
        {'text': 'Möchtest du auswandern?', 'yes': reverse('question', args=[2]), 'no': reverse('result_no')}, #1
        {'text': 'Kannst du dir vorstellen in 3 Ländern zu leben und dabei weniger als 183 Tage im Jahr pro Land zu bleiben?',
         'yes': reverse('question', args=[3]), 'no': reverse('question', args=[4])},
        {'text': 'Hattest du Bezugspunkte zu Deutschland wie Kinder, Frau oder Wohnung mit Schlüsselgewalt?',
         'yes': reverse('question', args=[5]), 'no': reverse('result')},
        {'text': 'Kannst du dir vorstellen im Ausland fest in einem Land zu leben?',
         'yes': reverse('result_yes'), 'no': reverse('result_no')},
        {'text': 'Kannst du die Bezugspunkte auflösen?', 'yes': reverse('result'),
         'no': reverse('result_no')}, # 5

    ]
    question = questions[question_number - 1]
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        answer = form.cleaned_data['answer']
        return redirect(question[answer])
    return render(request, 'website/berater.html', {'question': question, 'form': form})


def question(request, question_number):
    questions = [
        {'text': 'Möchtest du auswandern?', 'yes': reverse('question', args=[2]), 'no': reverse('question', args=[10])}, #1
        {'text': 'Kannst du dir vorstellen in 3 Ländern zu leben und dabei weniger als 183 Tage im Jahr pro Land zu bleiben?', 'yes': reverse('question', args=[3]), 'no': reverse('question', args=[4])},
        {'text': 'Hattest du Bezugspunkte zu Deutschland wie Kinder, Frau oder Wohnung mit Schlüsselgewalt?', 'yes': reverse('question', args=[5]), 'no': reverse('question', args=[8])},
        {'text': 'Kannst du dir vorstellen im Ausland fest in einem Land zu leben?', 'yes': reverse('question', args=[7]), 'no': reverse('question', args=[10])},
        {'text': 'Kannst du die Bezugspunkte auflösen?', 'yes': reverse('question', args=[8]), 'no': reverse('result_no')}, #5
        {'text': 'PP kommt generell in Frage, informiere bei unseren Experten', 'yes': reverse('result'), 'no': reverse('result')},
        {'text': 'Auswanderung mit festem Wohnsitz kommt in Frage, bitte informiere dich bei unseren Experten', 'yes': reverse('result'), 'no': reverse('result')},
        {'text': 'PP kommt in Frage', 'yes': reverse('result'), 'no': reverse('result')},#8
        {'text': 'Kein PP kommt in Frage', 'yes': reverse('result'), 'no': reverse('result')},#9
        {'text': 'Keine Auswanderung sinnvoll', 'yes': reverse('result'), 'no': reverse('result')}, #10
    ]
    question = questions[question_number-1]
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        answer = form.cleaned_data['answer']
        return redirect(question[answer])
    return render(request, 'question.html', {'question': question, 'form': form})


def result(request):
    return render(request, 'result.html')

def result_no(request):
    return render(request, 'result_no.html')

def result_yes(request):
    return render(request, 'result_yes.html')
