from django.urls import path
from .views import (
    QuestionListCreateAPIView,
    QuestionRetrieveDestroyAPIView,
    AnswerCreateAPIView,
    AnswerRetrieveDestroyAPIView
)

urlpatterns = [
    path('questions/', QuestionListCreateAPIView.as_view(), name='questions-list-create'),
    path('questions/<int:pk>/', QuestionRetrieveDestroyAPIView.as_view(), name='question-detail-delete'),
    path('questions/<int:pk>/answers/', AnswerCreateAPIView.as_view(), name='answer-create'),
    path('answers/<int:pk>/', AnswerRetrieveDestroyAPIView.as_view(), name='answer-detail-delete'),
]