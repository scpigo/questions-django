# API-сервис для вопросов и ответов

## Установка
1. создать файл `.env` идентичный файлу `.env.example`
2. в корне проекта выполнить команду `docker-compose up -d --build`
3. в контейнере `web` применить миграции выполнив команду `python manage.py migrate`
4. там же при необходимости создать администратора командой `python manage.py createsuperuser`
5. панель администратора доступна по адресу `http://localhost:7070/admin/`
6. тесты можно запустить в контейнере `web` командой `pytest -v`

## API методы
- `(GET) /api/questions/` - получить список вопросов
- `(POST) /api/questions/` - создать вопрос (поля: text - текст вопроса)
- `(GET) /api/questions/<question_id>/` - получить вопрос по его id
- `(DELETE) /api/questions/<question_id>/` - удалить вопрос
- `(POST) /api/questions/<question_id>/answers/` - создать ответ вопрос (поля: user_id: uuid пользователя, text - текст ответа)
- `(GET) /api/answers/<answer_id>/` - получить ответ по его id
- `(DELETE) /api/answers/<answer_id>/` - удалить ответ