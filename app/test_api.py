import pytest
from django.urls import reverse
from rest_framework import status
from uuid import uuid4
from api.models import Question, Answer

@pytest.mark.django_db
def test_create_question(api_client):
    data = {'text': 'тестовый вопрос'}
    response = api_client.post(
        reverse('questions-list-create'),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in response.data
    assert 'text' in response.data
    assert response.data['text'] == data['text']

@pytest.mark.django_db
def test_create_question_without_text(api_client):
    data = {}
    response = api_client.post(
        reverse('questions-list-create'),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_create_question_with_empty_text(api_client):
    data = {'text': ''}
    response = api_client.post(
        reverse('questions-list-create'),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_get_questions_list(api_client):
    Question.objects.create(text='тестовый вопрос 1')
    Question.objects.create(text='тестовый вопрос 2')
    response = api_client.get(reverse('questions-list-create'))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) >= 2

@pytest.mark.django_db
def test_get_question_detail_with_answers(api_client):
    question = Question.objects.create(text='тестовый вопрос')
    Answer.objects.create(question=question, user_id=uuid4(), text='тестовый ответ')
    response = api_client.get(reverse('question-detail-delete', args=[question.id]))
    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == question.id
    assert 'answers' in response.data
    assert len(response.data['answers']) == 1

@pytest.mark.django_db
def test_delete_question_and_answers(api_client):
    question = Question.objects.create(text='тестовый вопрос')
    Answer.objects.create(question=question, user_id=uuid4(), text='тестовый ответ')
    response = api_client.delete(reverse('question-detail-delete', args=[question.id]))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Question.objects.filter(id=question.id).exists()
    assert not Answer.objects.filter(question=question).exists()

@pytest.mark.django_db
def test_create_answer_for_existing_question(api_client):
    question = Question.objects.create(text='тестовый вопрос')
    data = {'user_id': str(uuid4()), 'text': 'тестовый ответ'}
    response = api_client.post(
        reverse('answer-create', args=[question.id]),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['text'] == data['text']
    assert response.data['question'] == question.id

@pytest.mark.django_db
def test_create_answer_for_nonexistent_question(api_client):
    data = {'user_id': str(uuid4()), 'text': 'тестовый ответ'}
    response = api_client.post(
        reverse('answer-create', args=[9999]),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_create_answer_without_text(api_client):
    question = Question.objects.create(text='тестовый вопрос')
    data = {'user_id': str(uuid4())}
    response = api_client.post(
        reverse('answer-create', args=[question.id]),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_create_answer_with_empty_text(api_client):
    question = Question.objects.create(text='тестовый вопрос')
    data = {'user_id': str(uuid4()), 'text': ''}
    response = api_client.post(
        reverse('answer-create', args=[question.id]),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_create_answer_without_user_id(api_client):
    question = Question.objects.create(text='тестовый вопрос')
    data = {'text': 'тестовый ответ'}
    response = api_client.post(
        reverse('answer-create', args=[question.id]),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_create_answer_with_wrong_user_id(api_client):
    question = Question.objects.create(text='тестовый вопрос')
    data = {'user_id': 'sfsdsrwer', 'text': 'тестовый ответ'}
    response = api_client.post(
        reverse('answer-create', args=[question.id]),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_get_answer_detail(api_client):
    question = Question.objects.create(text='тестовый вопрос')
    answer = Answer.objects.create(question=question, user_id=uuid4(), text='тестовый ответ')
    response = api_client.get(reverse('answer-detail-delete', args=[answer.id]))
    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == answer.id

@pytest.mark.django_db
def test_delete_answer(api_client):
    question = Question.objects.create(text='тестовый вопрос')
    answer = Answer.objects.create(question=question, user_id=uuid4(), text='тестовый ответ')
    response = api_client.delete(reverse('answer-detail-delete', args=[answer.id]))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Answer.objects.filter(id=answer.id).exists()