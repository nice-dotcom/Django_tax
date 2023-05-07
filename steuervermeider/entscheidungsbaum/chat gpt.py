
Diese Django app besteht aus einer views.py, urls.py und einer question.html. Könnte man den code vereinfachen oder übersichtlicher gestalten?


views.py:

from django.shortcuts import render, redirect

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html")

def berater(request):
    return render(request, 'website/berater.html')


def question(request, question_number):
    questions = [
        {'text': 'Möchtest du auswandern?', 'yes': '/question/3/', 'no': '/question/2/'},
        {'text': 'Möchtest du wenigstens dein Haus sanieren?', 'yes': '/question/3/', 'no': '/result/'},
        {'text': 'Möchtest du in Europa bleiben?', 'yes': '/result/', 'no': '/result/'}
    ]
    question = questions[question_number-1]
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer == 'yes':
            return redirect(question['yes'])
        elif answer == 'no':
            return redirect(question['no'])
    return render(request, 'question.html', {'question': question})


def result(request):
    return render(request, 'result.html')

urls.py:

from django.urls import path
from website import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('berater/', views.berater, name='berater'),
    path('question/<int:question_number>/', views.question, name='question'),
    path('result/', views.result, name='result'),
]


question.html:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<h1>Frage {{ question_number }}:</h1>
<p>{{ question.text }}</p>
<form method="post">
    {% csrf_token %}
    <button type="submit" name="answer" value="yes">Ja</button>
    <button type="submit" name="answer" value="no">Nein</button>
</form>

</body>
</html>

