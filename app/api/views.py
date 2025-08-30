from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer

class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer

class QuestionRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        question_id = self.kwargs.get("pk")
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise NotFound(detail="Вопрос не найден")
        serializer.save(question=question)

class AnswerRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
