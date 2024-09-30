from django.db import models

# Модель для хранения пользователей и их очков
class Player(models.Model):
    username = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.username


# Модель для хранения вопросов и правильных ответов
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text
