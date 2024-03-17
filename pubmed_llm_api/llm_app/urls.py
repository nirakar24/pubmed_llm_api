from django.urls import path
from .views import answer_question_with_abstracts, chat

urlpatterns = [
    path('answer/', answer_question_with_abstracts, name='answer'),
    path('chat/', chat, name='chat'),
    # Other URL patterns...
]