# Blog API

Простой REST API для блога на Django и DRF с JWT аутентификацией и комментариями.

## Запуск проекта

### Через Docker

1. Клонируйте репозиторий
2. Запустите контейнеры: docker compose up --build
3. Примените миграции: docker compose exec web python manage.py migrate
4. Создайте суперпользователя: docker compose exec web python manage.py createsuperuser
5. Откройте http://localhost:8000/
6.          http://127.0.0.1:8000/


### Локально без Docker

1. Создайте виртуальное окружение и активируйте его
2. Установите зависимости: pip install -r requirements.txt
3. Создайте файл .env с переменными окружения
4. Запустите локальный PostgreSQL
5. Примените миграции: python manage.py migrate
6. Запустите сервер: python manage.py runserver
7. Откройте http://127.0.0.1:8000/

## Документация

- Swagger UI: /swagger/
- ReDoc: /redoc/

