from django.shortcuts import render, redirect
from .models import Player, Question
from .forms import QuizForm

# Страница с тестом
def quiz_view(request):
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            score = 0
            # Проходим по всем вопросам
            for question in Question.objects.all():
                user_answer = form.cleaned_data.get(f'question_{question.id}')
                if user_answer == question.correct_answer:
                    score += 1
            # Сохраняем результат игрока
            Player.objects.create(username=request.POST['username'], score=score)
            return redirect('leaderboard')
    else:
        form = QuizForm()

    return render(request, 'ttesting/quiz.html', {'form': form})


def leaderboard_view(request):
    players = Player.objects.all().order_by('-score')
    return render(request, 'ttesting/leaderboard.html', {'players': players})