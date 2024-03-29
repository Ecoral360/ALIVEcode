from playground.views import index, code, blocs, robot, testing, newQuiz, mesQuiz, deleteQuiz, updateQuiz, deleteQuestion, updateQuestion, repQuiz, quizChoices
from django.urls import path, re_path

urlpatterns = [
    path('', index, name='index'),
    path('code', code, name='code'),
    path('blocs', blocs, name='blocs'),
    path('robot', robot, name='robot'),
    path('testing', testing, name='testing'),
    path('new_quiz', newQuiz, name='newQuiz'),
    #path('view_quiz', viewQuiz, name='viewQuiz'),
    path('mes_quiz', mesQuiz, name='repQuiz'),
    path('delete_quiz/<str:pk>', deleteQuiz, name='deleteQuiz'),
    path('update_quiz/<str:pk>', updateQuiz, name='updateQuiz'),
    path('view_quiz/delete', deleteQuestion.as_view(), name='deleteQuestion'),
    path('view_quiz/<str:pk>/update', updateQuestion, name='updateQuestion'),
    path('rep_quiz/<str:pk>', repQuiz, name='repQuiz'),
    path('quiz_choices', quizChoices, name='quizChoices')
]