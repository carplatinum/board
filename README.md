# Board - Backend доска объявлений

Простой backend для доски объявлений, реализованный на Django 5, Django REST Framework с JWT авторизацией, Celery, Redis, PostgreSQL, Docker и развертыванием в Yandex Cloud.

## Технологии

- Python 3.13, Django 5.x
- PostgreSQL, PgAdmin 4
- Django REST Framework + djangorestframework-simplejwt (JWT)
- Celery с Redis брокером
- Docker, Docker Compose
- GitHub Actions для CI/CD
- CORS support

## Структура проекта

- apps/users — управление пользователями
- apps/ads — объявления
- board/ — конфигурация Django проекта и celery.py 
- docker-compose.yml для локального запуска и разработки
- CI/CD workflow в `.github/workflows/ci-cd.yml`

## Установка и запуск

### 1. Клонирование и установка зависимостей

git clone <репозиторий>
cd board
poetry install


### 2. Создание и настройка .env файла

Создайте `.env` в корне проекта со следующими переменными:

SECRET_KEY=your-secret-key
DEBUG=True
POSTGRES_DB=board_db
POSTGRES_USER=board_user
POSTGRES_PASSWORD=board_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
REDIS_URL=redis://localhost:6379/0
CORS_ALLOWED_ORIGINS=http://localhost,http://127.0.0.1
ALLOWED_HOSTS=localhost,127.0.0.1


### 3. Запуск базы данных

- Запустите PostgreSQL (или через PgAdmin 4)
- Запустите Redis сервер (например, `redis-server`)

### 4. Примените миграции

poetry run python manage.py migrate


### 5. Запуск сервера разработки

poetry run python manage.py runserver


### 6. Запуск Celery воркера

poetry run celery -A board worker -l info


### 7. Запуск Celery beat (расписание задач)

poetry run celery -A board beat -l info


## Docker

Для локальной разработки и деплоя используется docker-compose.yaml и Dockerfile.

Запуск локально:

docker-compose up --build


## CI/CD

Настроена интеграция с GitHub Actions, которая автоматически строит и делаем деплой образа в Yandex Cloud VM.

---